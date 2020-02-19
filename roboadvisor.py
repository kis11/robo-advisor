# app/robo_advisor.py

import requests
import json

def to_usd(my_price):
  return f"${my_price:,.2f}"

symbol = input("Please enter a valid stock or crypto ticker here. Then hit enter.")

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"

response = requests.get(request_url)

#print(response.text)

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






#print("-------------------------")
print("SELECTED SYMBOL:" + " " + symbol)
#print("-------------------------")
#print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT:" + "  " + last_refreshed)
#print("-------------------------")
#print("LATEST DAY: 2018-02-20") #has to be a variable
print("LATEST CLOSE:" + "  " + to_usd(float(latest_close))) #variable
print("RECENT HIGH:" + "  " + to_usd(float(recent_high))) #variable
print("RECENT LOW:" + "  " + to_usd(float(recent_low))) #variable
#print("-------------------------")
#print("RECOMMENDATION: BUY!") #if < something, buy, if not , sell
#print("RECOMMENDATION REASON: TODO")
#print("-------------------------")
#print("HAPPY INVESTING!")
#print("-------------------------")
