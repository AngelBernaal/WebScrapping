import requests
from bs4 import BeautifulSoup

website_url = "https://www.themoviedb.org/tv?language=es"
result = requests.get(website_url)
content = result.text

soup = BeautifulSoup(content, "lxml")

series = soup.find_all("div", class_="card style_1")
for serie in series: 
    title = serie.find("h2").get_text(strip=True, separator=" ")
    rating = serie.find("div", class_="user_score_chart")['data-percent']
    date = serie.find("p").get_text(strip=True, separator=" ")
    print(f"Title: {title}, Date: {date}, Rating: {rating}")