from market import Market
import json
import requests

from GLOBAL_VARIABLES import CLOB

class Event():
    def __init__(self, info):
        self.info = info
        all_tokens = [t for m in info['markets'] for t in json.loads(m["clobTokenIds"])]
        books_by_token = self.get_books(all_tokens)
        self.markets = [Market(m, books_by_token) for m in info['markets']]

    def get_books(self, token_ids):
        response = requests.post(f'{CLOB}/books', json = [{"token_id": t} for t in token_ids]).json()
        return {b['asset_id']: b for b in response}

    def __str__(self):
        out = (f"Title: {self.info['title']}\n"
                f"End Date: {self.info['endDate']}\n\n")
        
        for i, market in enumerate(self.markets):
            out += f"Market {i + 1}:\n{str(market)}\n\n"
        return out
    
    def print_all_info(self):
        for key, value in self.info.items():
            print(f"{key:<15}: {value}")