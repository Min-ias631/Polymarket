
import requests
import json
from order_book import order_book

def get_gamma_data(URL):
    response = requests.get(URL).json()
    markets =  response['markets']
    return markets

def get_clob_token_ids(token_ids):
    response = requests.post("https://clob.polymarket.com/books", json=[{"token_id": t} for t in token_ids]).json()
    return response

if __name__ == "__main__":
    URL = "https://gamma-api.polymarket.com/events/slug/lol-t1-tl2-2026-06-28"
    markets = get_gamma_data(URL)
    clob = get_clob_token_ids(json.loads(markets[0]['clobTokenIds']))
    order_book = order_book(clob[0])
    print(clob[0])