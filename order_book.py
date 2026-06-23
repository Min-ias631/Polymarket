class order_book:
    def __init__(self, clob_data):
        self.market_id = clob_data['market'] #Identifies the market/question
        self.asset_id = clob_data['asset_id'] #Identifies the asset (e.g., YES or NO)
        self.timestamp = clob_data['timestamp'] 
        self.hash = clob_data['hash'] #Unique identifier for the order book state, useful for tracking changes

        self.bids = clob_data['bids'][::-1]  # Reverse to have highest bid first
        self.asks = clob_data['asks'][::-1]  # Reverse to have lowest ask first

        self.min_order_size = clob_data['min_order_size']
        self.tick_size = clob_data['tick_size']
        self.neg_risk = clob_data['neg_risk']
        self.last_trade_price = clob_data['last_trade_price']

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
        return self.display_depth(5)