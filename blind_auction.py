'''
A first-price sealed-bid auction (FPSBA) is a common type of auction. It is also known as blind auction. 
In this type of auction, all bidders simultaneously submit sealed bids so that no bidder knows the bid of any other participant. 
The highest bidder pays the price that was submitted
'''
#####Example output
'''
What is your name?: Alex
What is your bid?: $200
Are there any other bidders? Type 'yes or 'no'.
yes

What is your name?: Vincent
What is your bid?: $300
Are there any other bidders? Type 'yes or 'no'.
no
The winner is Vincent with a bid of $300
'''


from replit import clear 
from art import logo
print(logo)

bids = {} #new empty dictionary

def find_highest_bidder(bidding_record):
  highest_bid = 0 # checks for highest bidder amount
  # example, bidding_record = {"Angela": 123, "James": 321}
  # the for-loop, loops through the dictionary  
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder] # this gets the values of the keys
    # checking for highest bid amount  
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner_name = bidder #bidder is the key name
  print(f"The winner is {winner_name} with a bid of ${highest_bid}")

bidding_finished = True
while bidding_finished == True:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = False
    find_highest_bidder(bids)
  # below is for replit screen clearing
  elif should_continue == "yes":
    clear()
  
