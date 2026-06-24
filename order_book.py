class order_book:
    def __init__(self, clob_data):
        self.hash = clob_data['hash'] #Unique identifier for the order book state, useful for tracking changes

        self.bids = clob_data['bids'][::-1]  # Reverse to have highest bid first
        self.asks = clob_data['asks'][::-1]  # Reverse to have lowest ask first

    def display_depth(self, depth):
        ans = f"{'Depth':<7}{'Bid_Price':<12}{'Bid_Size':<12}{'Ask_Price':<12}{'Ask_Size':<12}"
        for i in range(depth):
            bid_price = self.bids[i]['price'] if i < len(self.bids) else "N/A"
            bid_size = self.bids[i]['size'] if i < len(self.bids) else "N/A"
            ask_price = self.asks[i]['price'] if i < len(self.asks) else "N/A"
            ask_size = self.asks[i]['size'] if i < len(self.asks) else "N/A"
            ans += (f"\n{str(i+1):<7}{str(bid_price):<12}{str(bid_size):<12}{str(ask_price):<12}{str(ask_size):<12}")
        return ans

    def __str__(self):
        return self.display_depth(3)