from bs4 import BeautifulSoup
import requests
import lxml

# i love you, you got this ! don't give up :)

THRESHOLD = 70
PRODUCT_URL = "https://www.amazon.com/Neewer-Ring-Light-Kit-Self-Portrait/dp/B01LXDNNBW/ref=sr_1_1_sspa?crid=KRNYKXPQVBUT&keywords=ring+light&qid=1677932315&sprefix=ring+%2Caps%2C292&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExT1hFVFJBWkI2T1VVJmVuY3J5cHRlZElkPUEwODcxNjE4MUFIWVNOVDJLMkxWUyZlbmNyeXB0ZWRBZElkPUEwNzk2OTEwMU5FUDJFUFM2VjU5RyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
           "Accept-Language": "en-US,en-GB;q=0.9,en;q=0.8,de-DE;q=0.7,de;q=0.6"}
product_response = requests.get(url=PRODUCT_URL, headers=headers)
# product_response.encoding = "utf-8"
soup = BeautifulSoup(product_response.text, "lxml")

result = soup.find(name="span", class_="a-offscreen").get_text()
title = soup.find(id="productTitle").get_text().strip()
current_price = float(result[1:])

if current_price <= THRESHOLD:
    print(f"GO BUY THE {title} GIRL, ONLY {result}")
else:
    print(f"nvm ugh, {title} too expensive: {result}")