import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
# STOCK_NAME = "FB"
COMPANY_NAME = "Tesla"

# Stock API
STOCK_API_KEY = "STOCK-API KEY HERE"  # get your own API KEY from https://www.alphavantage.co/
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

# News API

NEWS_API_KEY = 'YOUR API KEY FROM NEWSAPI.ORG HERE'  # Get your own API KEY From https://newsapi.org/
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# twilio - used to send SMS
ACCOUNT_SID = 'YOUR TWILIO ACCOUNT SID HERE'  # Get it from twilio.com
AUTH_TOKEN = 'YOUR TWILIO AUT TOKEN HERE'  # Get it from twilio.com

# Get yesterday's closing stock price.
stock_params = {
    'function': "TIME_SERIES_DAILY",
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']

# Find The Difference
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Difference in Percentage
diff_percent = round((difference / float(yesterday_closing_price)) * 100)

print(diff_percent)

# use the News API to get articles related to the COMPANY_NAME if the Difference is greater than 5 Percent
if abs(diff_percent) > 5:
    news_params = {
        "apikey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]  # Only 3 Articles

# Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}% \nHeadline: {article['title']} \nBrief: {article['description']}" for article in three_articles]

# Send each article as a separate message via Twilio.
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for current_article in formatted_articles:
        message = client.messages.create(
            body=current_article,
            from_='COPY AND PASTE YOUR PHONE NUMBER FROM TWILIO HERE',
            to='PUT RECEIVER PHONE HERE'
        )
        print(message.sid)

