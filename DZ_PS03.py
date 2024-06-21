from bs4 import BeautifulSoup
import requests
from googletrans import Translator


# Функция для получения случайного слова и его определения с сайта randomword.com
def get_word():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        if response.status_code != 200:  # Проверка на успешность запроса
            return None
        soup = BeautifulSoup(response.content, 'html.parser')
        word = soup.find('div', id="random_word").text.strip()
        word_definition = soup.find('div', id="random_word_definition").text.strip()
        return {
            "word": word,
            "definition": word_definition
        }
    except Exception as e:
        print(f"Произошла ошибка {e}")
        return None


# Основная функция для игры в угадывание слов
def word_game():
    print("Добро пожаловать в игру 'Слова'")
    translator = Translator()  # Инициализация переводчика
    while True:
        word_dict = get_word()
        if not word_dict:  # Проверка, получили ли мы слово и его определение
            print("Не удалось получить слово. Попробуйте еще раз.")
            continue
        word = word_dict.get("word")
        word_definition = word_dict.get("definition")

        # Перевод слова и его определения на русский язык
        translated_word = translator.translate(word, src='en', dest='ru').text
        translated_definition = translator.translate(word_definition, src='en', dest='ru').text

        print(f"Значение слова: {translated_definition}")
        user_input = input("Что это за слово?\n").lower()
        if user_input == translated_word.lower():
            print("Поздравляю, вы угадали!")
        else:
            print(f"Неправильно, было загадано это слово: {translated_word}")

        play_again = input("Хотите сыграть еще раз? (Да/Нет)").lower()
        if play_again != "да":
            break

    print("Спасибо за игру!")


word_game()
