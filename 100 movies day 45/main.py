from bs4 import BeautifulSoup
import requests


# with open("website.html", encoding="utf8") as file:
#     soup = BeautifulSoup(file, "html.parser")
#
# all_anchor_tags = soup.find_all(name="a")
#
# # for tag in all_anchor_tags:
# #     print(tag.get("href"))
#
# heading = soup.find(id="name")
# print(heading)

url = "https://news.ycombinator.com/"
response = requests.get(url)
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

scores = []
for item in soup.find_all("span", "score"):
    scores.append(int(item.getText().split()[0]))
max_score = max(scores)

a_contents = []
for tag in soup.find_all("a"):
    a_contents.append(tag.getText())
lst = a_contents[10:]
headlines = []
for index, text in enumerate(lst):
    if text == "":
        headlines.append(lst[index+1])

links = []
titleline_spans = soup.find_all('span', class_='titleline')
for span in titleline_spans:
    a_tags = span.find_all('a')
    for a in a_tags:
        href = a.get('href')
        if "https:" in href:
            links.append(href)

if len(headlines) > len(links) or len(headlines) < len(links):
    difference = len(headlines) - len(links)
    most_popular_index = scores.index(max_score)
    most_popular_headline = headlines[most_popular_index]
    most_popular_link = links[most_popular_index - difference]
else:
    most_popular_index = scores.index(max_score)
    most_popular_headline = headlines[most_popular_index]
    most_popular_link = links[most_popular_index]

most_popular_index += 2

# print(links)
# print(len(headlines), len(links))
print(f"{most_popular_index}, {most_popular_headline}, {most_popular_link}")

#IT DOESNT WORK, FIX


