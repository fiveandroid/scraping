import requests
from bs4 import BeautifulSoup

url = "https://listado.mercadolibre.com.mx/zapatillas-hombre#D[A:zapatillas%20hombre]"

response = requests.get(url)

if response.status_code == 200:
    print("Obtuvimos la pagina")

    soup = BeautifulSoup( response.text, 'html.parser')

    productos = soup.find_all('div', class_="andes-card poly-card poly-card--grid-card andes-card--flat andes-card--padding-0 andes-card--animated")

    print (len(productos))

    for producto in productos:
        titulo= producto.find('h2', "poly-box poly-component__title")

        if titulo:
            print( titulo.text.strip())

else:
    print("Hubo un Error")

    