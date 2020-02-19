# app/robo_advisor.py

import requests
import json
import csv
import os
from datetime import datetime
from datetime import date
from dotenv import load_dotenv

now = datetime.now()
today = date.today()
current_time = now.strftime("%H:%M:%S")
current_date = today.strftime("%Y-%m-%d")

load_dotenv()
apikey = os.getenv("ALPHAVANTAGE_API_KEY")

def to_usd(my_price):
  return f"${my_price:,.2f}"

symbol = input("Please enter a valid stock or crypto ticker here. Then hit enter.")

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={apikey}"

response = requests.get(request_url)


parsed_response = json.loads(response.text)

tsd = parsed_response["Time Series (Daily)"]
dates = list(tsd.keys())
latest_day = dates[0]
md = parsed_response["Meta Data"]
last_refreshed = md["3. Last Refreshed"]
latest_close = tsd[latest_day]["4. close"]

high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    low_price = tsd[date]["3. low"]
    high_prices.append(float(high_price))
    low_prices.append(float(low_price))


recent_high = max(high_prices)
recent_low = min(low_prices)

csv_filepath = os.path.join(os.path.dirname(__file__), "data", "prices.csv")
csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_filepath, "w") as csv_file:
  writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
  writer.writeheader()
  for date in dates:
    daily_prices = tsd[date]
    writer.writerow({
      "timestamp": date,
      "open": daily_prices["1. open"],
      "high": daily_prices["2. high"],
      "low": daily_prices["3. low"],
      "close": daily_prices["4. close"],
      "volume": daily_prices["5. volume"],
    })
      







print("-------------------------")
print("SELECTED SYMBOL:" + " " + symbol)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT:" + "  " + current_date + " " +  "at" + " " + str(current_time))
#print("-------------------------")
print("LATEST DAY:" + "  " + str(latest_day)) #has to be a variable
print("LATEST CLOSE:" + "  " + to_usd(float(latest_close))) #variable
print("RECENT HIGH:" + "  " + to_usd(float(recent_high))) #variable
print("RECENT LOW:" + "  " + to_usd(float(recent_low))) #variable
print("-------------------------")
#print("RECOMMENDATION: BUY!") #if < something, buy, if not , sell
#print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
