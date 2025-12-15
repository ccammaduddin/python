# ☕️ Loyalty Points Engine Challenge
#
# RULES:
# • Each whole dollar spent earns 3 points
# • Tiers:
#     < 100 pts   →  Bronze
#     100-499 pts → Silver
#     ≥ 500 pts   →  Gold
#
# STEPS:
# 1. Define earn_points(price) → returns points for one purchase
# 2. Define tier_label(points) → returns "Bronze" / "Silver" / "Gold"
# 3. Given the hard-coded list `purchases`,
#    loop through it, call earn_points() for each amount,
#    and add the result to total_points.
# 4. After the loop, call tier_label(total_points)
# 5. Print 'Loyalty Summary': 
#       • Total dollars spent
#       • Total points earned
#       • Final tier

# Purchase history (e.g., 3.75, 7.20, etc.)

purchases = [12.50, 40.25, 5.90, 80.00, 25.45]

def earn_points(price):
    points = int(price) * 3
    return points

def tier_label(points):
    if points < 100:
        return "Bronze"
    elif points < 500:
        return "Silver"
    else:
        return "Gold"

total_spent = 0.0
total_points = 0

for amount in purchases:
    total_spent += amount
    total_points += earn_points(amount)

final_tier = tier_label(total_points)

print("Loyalty Summary")
print("--------------")
print(f"Total Dollars Spent: ${total_spent:.2f}")
print(f"Total Points Earned: {total_points} pts")
print(f"Final Tier: {final_tier}")