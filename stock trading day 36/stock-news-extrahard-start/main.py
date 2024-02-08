import requests
import datetime as df
from twilio.rest import Client
import os # use it to add envionment variables and get them


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

AV_API_KEY = "apikey"
AV_ENDPOINT = "https://www.alphavantage.co/query"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "apikey2"

account_sid = "accsid"
auth_token = "authtoken"
twilio_number = "twilionumber"
my_number = "mynumber"


def percentage(a, b):
    """
    Minus sign indicates that previous money was bigger than last money, meaning the stock's worth decreased for that %
    :param a: last money
    :param b: previous money
    """
    difference = float(a) - float(b)
    resultat = (difference / float(a)) * 100
    return round(resultat, 2)


today = df.date.today()
yesterday = today - df.timedelta(days=1)

# # STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parametres0 = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": AV_API_KEY
}
response0 = requests.get(url=AV_ENDPOINT, params=parametres0)
response0.raise_for_status()

last_date = list(response0.json()["Time Series (Daily)"])[0]
the_date_before = list(response0.json()["Time Series (Daily)"])[1]

last_money = response0.json()["Time Series (Daily)"][last_date]['4. close']
previous_money = response0.json()["Time Series (Daily)"][the_date_before]['4. close']

result = percentage(last_money, previous_money)

# # STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

parametres1 = {
    "q": f"{STOCK} OR {COMPANY_NAME}",
    "apiKey": NEWS_API_KEY,
}
response1 = requests.get(url=NEWS_ENDPOINT, params=parametres1)
response1.raise_for_status()

escape = ("<li>", "<ol>", "</li>", "</a>", "<a", 'target="_blank"')

if abs(result) >= 5:
    client = Client(account_sid, auth_token)
    for index in range(3):
        headline = response1.json()["articles"][index]["title"]
        description = response1.json()["articles"][index]["description"]
        for sign in escape:
            description = description.replace(sign, "")
        url_more_info = response1.json()["articles"][index]["url"]

        # # STEP 3: Use https://www.twilio.com
        # Send a seperate message with the percentage change and each article's title and description
        # to your phone number.

        send_this = (f"{STOCK}: {result}%\n"
                     f"Headline: {headline},\n"
                     f"Brief: {description}\n")

        message = client.messages.create(
            body=send_this,
            from_=twilio_number,
            to=my_number
        )
        print(message.sid)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
