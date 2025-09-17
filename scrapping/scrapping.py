import requests
from bs4 import BeautifulSoup

website_url = "https://www.themoviedb.org/movie/top-rated?language=es" # URL de la pagina web que queremos scrapear

result = requests.get(website_url) # hacemos una solicitud GET a la URL
content = result.text # obtenemos el contenido HTML de la pagina

soup = BeautifulSoup(content, "lxml") # parseamos el contenido HTML con BeautifulSoup usando el parser lxml
# print(soup.prettify()) 

movies = soup.find_all("div", class_="card style_1") # esto obtiene todas las peliculas por el div con clase card style_1
for movie in movies: # iteramos sobre cada pelicula encontrada
    title = movie.find("h2").get_text(strip=True, separator=" ") # obtenemos el titulo de la pelicula
    rating = movie.find("div", class_="user_score_chart")['data-percent'] # obtenemos el rating de la pelicula
    date = movie.find("p").get_text(strip=True, separator=" ") # obtenemos la fecha de la pelicula
    print(f"Title: {title}, Date: {date}, Rating: {rating}") # imprimimos el titulo, fecha y rating de cada pelicula