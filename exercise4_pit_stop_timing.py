# 🏁 Pit Stop Timing Optimizer 🔧
#
# 1. Ask the user for the total race time in seconds.
# 2. Ask how many pit stops were made.
# 3. Ask for the average pit stop duration (in seconds).
#
# Then:
# - Calculate the total pit stop time.
# - Calculate the percentage of the race spent in the pits.
# - Round the percentage to 2 decimal places.
#
# Finally, print all of the following:
# - Total pit stop time in seconds
# - Percentage of race time spent in pits
# - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"

total_race_time = float(input("Enter Total race time in seconds : "))
pit_scores = int(input("Enter number of pit stops made : "))
avg_pit_duration = float(input("Enter average pit stop duration in seconds : "))

total_pit_time = pit_scores * avg_pit_duration
percentage_pit_time = (total_pit_time / total_race_time) * 100
rounded_percentage = round(percentage_pit_time, 2)

print("Total pit stop time in seconds:", total_pit_time)
print("Percentage of race time spent in pits:", rounded_percentage, "%")

if rounded_percentage > 5:
    print("You need a new pit crew. 🛠️")