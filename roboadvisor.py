# app/robo_advisor.py

import requests
import json


request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"

response = requests.get(request_url)

#print(response.text)

parsed_response = json.loads(response.text)

last_refreshed = ((parsed_response["Meta Data"]["3. Last Refreshed"]))



#print("-------------------------")
#print("SELECTED SYMBOL: XYZ")
#print("-------------------------")
#print("REQUESTING STOCK MARKET DATA...")
#print("REQUEST AT: 2018-02-20 02:00pm")
#print("-------------------------")
#print("LATEST DAY: 2018-02-20") #has to be a variable
#print("LATEST CLOSE: $100,000.00") #variable
#print("RECENT HIGH: $101,000.00") #variable
#print("RECENT LOW: $99,000.00") #variable
#print("-------------------------")
#print("RECOMMENDATION: BUY!") #if < something, buy, if not , sell
#print("RECOMMENDATION REASON: TODO")
#print("-------------------------")
#print("HAPPY INVESTING!")
#print("-------------------------")
