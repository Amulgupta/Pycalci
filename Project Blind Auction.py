# Blind Auction

# The objective is to write a program that will collect the names and bids of different people. The program should ask for each bidder's name and their bid individually.


from replit import clear

#HINT: You can now call clear() to clear the output in the console. It is a useful method of replit.

#lPrinting logo

from art import logo
print(logo)

#Start

print("Welcome to the secret auction program.")
auction = {}

result = True
while(result):
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  auction[name] = bid
  reply = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  if(reply == "no"):
    result = False
  clear()

winner = ""
winning_bid = 0
for name in auction:
  if auction[name] > winning_bid:
    winner = name
    winning_bid = auction[name]

print(f"The winner is {winner} with a bid of ${winning_bid}")
