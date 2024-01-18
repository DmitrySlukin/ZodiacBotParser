import requests
from bs4 import BeautifulSoup


def parser(url):
    get_querry = requests.get(url)  # Формируем get-запрос к странице с нашим url
    soup = BeautifulSoup(get_querry.text, 'html.parser')  # Читаем html страницу как текст
    horoscope = soup.find('p', class_="mtZOt")  # выделяем из html-кода только кусочек с текстом гороскопа
    return [content.text for content in horoscope]  # Возвращаем очищенный текст гороскопа от лишних тегов
