from bs4 import BeautifulSoup
import requests

def scrapping(url):
    # делаем запрос и получаем html
    page = requests.get(url)
    page.encoding = 'utf8'
    html_content = page.text

    #получаем картинки
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    list_img = [url + img.attrs.get("src") for img in soup.find_all("img")] +\
            [url + teg.attrs.get("background") for teg in soup.find_all() if teg.attrs.get("background") != None]
    html_img = {img for img in list_img}

    #получаем текст
    html_text = {teg.text for teg in soup.find_all() if teg.text != ''}

    print(html_content, html_img, html_text)
    
#https://lysenkokris.github.io/Project-Sem1/ тестовый сайт
scrapping(input())
