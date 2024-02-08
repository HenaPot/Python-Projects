from bs4 import BeautifulSoup
import requests


url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)
content = response.text
soup = BeautifulSoup(content, "html.parser")

headlines = soup.find_all("h3", "title")
formatted_headlines = [headline.getText() for headline in headlines]
formatted_headlines.reverse()

with open("must_watch_movies.txt", "w", encoding="utf-8") as movies_file:
    for movie in formatted_headlines:
        movies_file.write(f"{movie}\n")