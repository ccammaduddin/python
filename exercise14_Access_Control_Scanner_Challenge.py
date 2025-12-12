# 🛂 Access Control Scanner Challenge
#
# 1. Create a set of revoked badge numbers.
# 2. Create two empty lists: "approved" and "denied".
# 3. Start a loop to collect visitor info:
#    - Ask for the visitor's name (or type "done" to finish).
#    - If the name is "done", exit the loop.
#    - Otherwise, ask for their badge number.
#    - Check if the badge is revoked:
#        • If revoked: add the name to "denied" and display "ACCESS DENIED".
#        • If not: add the name to "approved" and display "ACCESS GRANTED".
# 4. Print the final "Access Summary" for "✅ Approved Visitors" & "⛔️ Denied Visitors":
#    - Sort both lists alphabetically.
#    - Display the total number of approved and denied visitors.

revoked_badges = {9211, 8923, 9973, 1244, 8733, 7112, 2981} 
approved = []
denied = []

while True:
    name = input("Enter visitor's name (or type 'done' to finish): ")
    if name.lower() == 'done':
        break
    badge_number = int(input("Enter 4 digits badge number: "))
    if badge_number in revoked_badges:
        denied.append(name)
        print("ACCESS DENIED")
    else:
        approved.append(name)
        print("ACCESS GRANTED")

print("\nAccess Summary:")
approved.sort()
print("✅ Approved Visitors:")
for visitor in approved:
    print(f"- {visitor}")

denied.sort()
print("⛔️ Denied Visitors:")
for visitor in denied:
    print(f"- {visitor}")

access_summary = len(approved) + len(denied)
print(f"\nTotal Visitors Processed: {access_summary}")