from bs4 import BeautifulSoup
import requests
from googletrans import Translator
def get_word():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        print(response.status_code)
        soup = BeautifulSoup(response.content, 'html.parser')
        word = soup.find('div', id="random_word").text.strip()
        word_definition = soup.find('div', id="random_word_definition").text.strip()
        return{
            "word": word,
            "definition": word_definition
        }
    except Exception as e:
        print(f"Произошла  ошибка {e}")

def word_game():
    print("Добро пожаловать в игру 'Слова'")
    while True:
        word_dict = get_word()
        word = word_dict.get("word")
        word_definition = word_dict.get("definition")
        print(f"Значение слова: {word_definition}")
        user_input = input("Что это за слово?\n").lower()
        if user_input == word:
            print("Поздравляю, вы угадали!")
        else:
            print(f"Неправильно, было загадано это слово {word}")
        play_again = input("Хотите сыграть еще раз? (Y/N)")
        if play_again.lower() != "y":
            break
        else:
            print("Спасибо за игру!")

word_game()