# app/robo_advisor.py

import requests
import json
import csv
import os
import plotly
import plotly.graph_objs as go
from datetime import datetime
from datetime import date
from dotenv import load_dotenv
import pandas as pd

def to_usd(my_price):
  """
    Changes numbers into USD dollar format.

    Params:
      my_price (numeric), the number you want to be turned into dollar formatting

    Example:
      to_usd(3) 
      to_usd(4.49)
  """
  return f"${my_price:,.2f}"
def write_to_csv():
  """
    Writes stock information to CSV.

    Params:
        none
  """
  global csv_filepath,csv_headers,df
  csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")
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
  df = pd.read_csv(csv_filepath)
  return df  
def check_if_buy(latest_close,yearly_high):
  if float(latest_close) < 0.95*(yearly_high):
    recommendation = "Buy!"
    return recommendation
  else:
    recommendation = "Don't Buy."
    return recommendation
def get_response(symbol):
  """
    Gets stock information from API and turns into digestible data for the system.

    Params:
      symbol (your stock ticker)
    Example:
      get_response(GS) # gets you Goldman Sachs' stock data.
  """
  global apikey,request_url,weekly_url,response,weeklyresponse,parsed_response,parsed_weekly
  e = "Error, try again."
  apikey = os.getenv("ALPHAVANTAGE_API_KEY", default = "OOPS")
  while True:
    try:
      request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={apikey}"
      weekly_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={symbol}&apikey={apikey}"
      response = requests.get(request_url)
      weeklyresponse = requests.get(weekly_url)
      parsed_response = json.loads(response.text)
      parsed_weekly = json.loads(weeklyresponse.text)
      if "Error Message" not in response.text:
        break
      print("Sorry, we couldn't find that symbol. Please try again with a valid ticker.")
    except Exception as e:
      print(e)
  return parsed_response

if __name__=="__main__":
  now = datetime.now()
  today = date.today()
  current_time = now.strftime("%H:%M:%S")
  current_date = today.strftime("%Y-%m-%d")

  apikey = os.getenv("ALPHAVANTAGE_API_KEY", default = "OOPS")

  e = "Error, try again."
  symbol = input("Please enter your ticker: ")
  get_response(symbol)

  tsd = parsed_response["Time Series (Daily)"]
  tsw = parsed_weekly["Weekly Time Series"]
  dates = list(tsd.keys())
  latest_day = dates[0]
  weeklydates = list(tsw.keys())[0:53]
  md = parsed_response["Meta Data"]
  last_refreshed = md["3. Last Refreshed"]
  latest_close = tsd[latest_day]["4. close"]

  weekly_high_prices = []
  weekly_low_prices = []

  for date in weeklydates:
      weekly_high_price = tsw[date]["2. high"]
      weekly_low_price = tsw[date]["3. low"]
      weekly_high_prices.append(float(weekly_high_price))
      weekly_low_prices.append(float(weekly_low_price))

  yearly_high = max(weekly_high_prices)
  yearly_low = min(weekly_low_prices)

  write_to_csv() 

  if float(latest_close) < 0.95*(yearly_high):
    recommendation = "Buy!"
  else:
    recommendation = "Don't Buy."

  if recommendation == "Buy!":
    rationale = "Stock is trading below 95 percent of its 52 week high."
  else:
    rationale = "Stock is trading near its most recent high. Might be overvalued."

  print("-------------------------")
  print("SELECTED SYMBOL:" + " " + symbol)
  print("-------------------------")
  print("REQUESTING STOCK MARKET DATA...")
  print("REQUEST AT:" + " " + current_date + " " +  "at" + " " + str(current_time))
  print("-------------------------")
  print("LATEST DAY:" + " " + str(latest_day)) #has to be a variable
  print("LATEST CLOSE:" + " " + to_usd(float(latest_close))) #variable
  print("52 WEEK HIGH:" + " " + to_usd(float(yearly_high))) #variable
  print("52 WEEK LOW:" + " " + to_usd(float(yearly_low))) #variable
  print("-------------------------")
  print("RECOMMENDATION:" + " " + recommendation) #if < something, buy, if not , sell
  print("RECOMMENDATION REASON:" + " " + rationale)
  print("-------------------------")
  print("HAPPY INVESTING!")
  print("-------------------------")

  plotly.offline.plot({
      "data": [go.Scatter(x=df['timestamp'], y=df['high'])],
      "layout": go.Layout(title="Recent stock price fluctuation for" + " " + symbol)
  }, auto_open=True)
