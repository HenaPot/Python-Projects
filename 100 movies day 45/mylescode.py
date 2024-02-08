from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for article in articles:
    text = article.getText()
    article_texts.append(text)
    link = article.find(name="a").get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts, len(article_texts))
print(article_links, len(article_links))
print(article_upvotes, len(article_upvotes))

