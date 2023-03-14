import requests
import time

while True:
    url = 'https://api.coinbase.com/v2/prices/BTC-USD/spot'
    response = requests.get(url)

    data = response.json()
    price = data['data']['amount']

    print(f"Current BTC price: {price} USD")
    
    # wait for 10 seconds before getting the price again
    time.sleep(1)
