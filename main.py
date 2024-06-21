from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

# links = soup.find_all("a")
# for link in links:
    #print(link)
    # print(link.get('href'))

text = soup.find_all("span", class_="text")
# for quote in text:
#     print(quote.text)

autors = soup.find_all("small", class_="author")
# for autor in autors:
#     print(autor.text)

for i in range(len(text)):
    print(f"Цитата номер {i+1}: \n {text[i].text} \n Автор цитаты:{autors[i].text}")