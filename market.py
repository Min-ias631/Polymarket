from order_book import order_book
import json


class Market():
    def __init__(self, info, books_by_token):
        self.info = info
        self.order_books = [
            order_book(books_by_token[t])
            for t in json.loads(info["clobTokenIds"])
        ]
    
    def __str__(self):
        return (f"Question: {self.info['question']}\n"
                f"End Date: {self.info['endDate']}\n"
                f"Order Book 1: {self.order_books[0]}\n"
                f"Order Book 2: {self.order_books[1]}")
    
    def print_all_info(self):
        for key, value in self.info.items():
            print(f"{key:<15}: {value}")