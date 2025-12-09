# 🕹️ Arcade Day Pass Tracker — Challenge Steps
#
# 1) Create variables to store:
#    - customer name
#    - number of passes
#    - tokens per pass
#    - price per pass
#    - tokens required per game
#
# 2) Calculate:
#    - total tokens
#    - total cost
#    - games available  (use 'floor division' to get a whole number)
#
# 3) Print a summary with:
#    - customer name
#    - passes bought
#    - total tokens
#    - total cost
#    - games available


customer_name = "Ammad"
number_of_passes = 12
tokens_per_pass = 10
price_per_pass = 5.00
tokens_required_per_game = 2
total_tokens = number_of_passes * tokens_per_pass
total_cost = number_of_passes * price_per_pass
games_available = total_tokens // tokens_required_per_game

print("Customer Name:", customer_name)
print("Passes Bought:", number_of_passes)
print("Total Tokens:", total_tokens)
print(f"Total Cost: ${total_cost:.2f}")
print("Games Available:", games_available)