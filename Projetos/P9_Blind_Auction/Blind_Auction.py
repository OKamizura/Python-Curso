from Blind_Auction_Art import logo
print(logo)

def find_the_greatest_value(bidding_dict):
  highest_bid = -1
  winner = ""
  for bidder in bidding_dict:
    bid_amount = bidding_dict[bidder]
    if bid_amount >= highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {}
continue_bidding = True

while continue_bidding:
  name = input("What's ya name?: ")
  bid = int(input("Whats's ya bid?: $"))
  bids[name] = bid

  shoud_continue = input("Are there other biders? Type 'yes' or 'no'. \n").lower()

  if shoud_continue == "no":
    continue_bidding = False
    find_the_greatest_value(bids)
  elif shoud_continue == "yes":
    print("\n" * 20)
  
