import requests
from pprint import pprint
from datetime import datetime, timedelta
from twilio.rest import Client
import time, os
from dotenv import load_dotenv

load_dotenv()

STOCK_NAME = "VST"
COMPANY_NAME = "Vistra Corp"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_APIKEY = os.getenv('ALPHADVANTAGE_APIKEY')
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_APIKEY = os.getenv('NEWSAPI_APIKEY')

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_APIKEY,
    "outputsize": "compact"
}

news_parameters = {
    "apiKey": NEWS_APIKEY,
    "q": COMPANY_NAME,
    "pageSize": 3,
    "page": 1
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
data = response.json()

# Get the list of dates (keys) from the data
dates = list(data["Time Series (Daily)"].keys())
# First item in the list will be the most recent trading day
yesterday_closing_price = float(data["Time Series (Daily)"][dates[0]]["4. close"])
print(yesterday_closing_price)

day_before_yesterday_closing_price = float(data["Time Series (Daily)"][dates[1]]["4. close"])
print(day_before_yesterday_closing_price)

difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)
print(difference)

percentage_difference = (difference / yesterday_closing_price) * 100
print(percentage_difference)

if percentage_difference > 5:
    print("Top news for :", COMPANY_NAME)

    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    news_data = response.json()

# Create a list of articles
news_articles = []
for article in news_data["articles"]:
    news_articles.append({
        "title": article["title"],
        "description": article["description"]
    })


account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

client = Client(account_sid, auth_token)

for article in news_articles:
    print(article)
    sign = "🔺" if yesterday_closing_price > day_before_yesterday_closing_price else "🔻"
    message = client.messages.create(
        body=f"{STOCK_NAME}: {sign}{percentage_difference:.1f}%\nHeadline: {article['title']}\nBrief: {article['description']}",
        from_="+12316802776",
        to="+918017894299"
    )
    time.sleep(5)

