import os

bidder_list = {}
other = True
while other is True:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))
    bidder_list[name] = bid

    other_bidder = input("Are there other users who want to bid? yes/no: ").lower()
    if other_bidder == "yes":
        other = True
    else:
        other = False
        bid_prices = list(bidder_list.values())
        bidder_names = list(bidder_list.keys())
        max_bid_price = max(bid_prices)
        max_bidder_name = bidder_names[bid_prices.index(max_bid_price)]
        print(f"Highest bidder is {max_bidder_name} with a bid of ${max_bid_price}")