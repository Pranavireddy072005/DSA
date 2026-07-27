def MaxProfit(self,prices):
    min_price=float('-inf')
    max_price=0
    for price in prices:
        min_price=min(min_price,price)
        max_price=max(max_price,price-min_price)
    return max_price