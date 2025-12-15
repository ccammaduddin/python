# 🐾 Dog Bus Tracker — Challenge Steps
#
# 1. Start with a bus dictionary holding current passengers.
#    - Each seat number (1, 2, 3, ...) is a key
#    - Each value is another dictionary with each pet's:
#        • name
#        • breed
#        • pickup time
#        • dropoff time
#
# 2. Print a starting roster showing each pet’s seat, name, and pickup time.
#
# 3. Add one new pet if there’s room on the bus.  
#    - Use MAX_SEATS to limit capacity.  
#    - Dynamically assign the next seat number.  
#    - Print the updated roster showing all pets after pickup.  
#
# 4. Ask which pet leaves early.  
#    - Remove that pet from the bus.  
#    - Print a message saying they’ve headed home.  
#
# 5. Print a final roster listing the remaining pets and their dropoff times.  


bus = {
    '1': {'name': 'Fido', 'breed': 'Labrador', 'pickup_time': '9:00 AM', 'dropoff_time': '5:00 PM'},
    '2': {'name': 'Whiskers', 'breed': 'Siamese', 'pickup_time': '9:15 AM', 'dropoff_time': '4:30 PM'},
    '3': {'name': 'Rex', 'breed': 'German Shepherd', 'pickup_time': '9:30 AM', 'dropoff_time': '5:15 PM'},
}

for seat, info in bus.items():
    print(f"Seat {seat}: {info['name']} picked up at {info['pickup_time']}")

MAX_SEATS = 5

if len(bus) <= MAX_SEATS:
    new_seat = str(len(bus) + 1)
    new_pet = {'name': 'Buddy', 'breed': 'Beagle', 'pickup_time': '10:00 AM', 'dropoff_time': '4:00 PM'}
    bus[new_seat] = new_pet
    print(f"{new_pet['name']} boards at {new_pet['pickup_time']}")
else:
    print("No more seats available on the bus.")


print("\n-- Roster after pickup --")
for seat, info in bus.items():
  print(f"Seat {seat}: {info['name']}")

remove_name = input("\nWho goes home early? ").strip().lower()

seat_to_remove = 0
for seat, info in bus.items():
  if info['name'].lower() == remove_name:
    seat_to_remove = seat
    break

if seat_to_remove:
  gone = bus.pop(seat_to_remove)
  print(f"\n👋  {gone['name']} (seat {seat_to_remove}) heads home early.")
else:
  print(f"\n⚠️  No passenger name '{remove_name}' on the bus.")


print("\n-- Final roster --")
for seat, info in bus.items():
  print(f"Seat {seat}: {info['name']} (drop-off {info['dropoff_time']})")

