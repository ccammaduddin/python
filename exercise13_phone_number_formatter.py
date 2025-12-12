# 📱 Phone Number Formatter
#
# 1. Ask the user to enter a U.S. phone number in **any format**.
# 2. Use .strip() to remove any leading/trailing spaces.
# 3. Replace common separators (-, (, ), .) with spaces.
# 4. Use .split() to break into chunks, then .join() to merge the digits.
# 5. Check if the cleaned number has **exactly 10 digits**.
# 6. If yes, format it like this: (123) 456-7890
# 7. If not, print an error message: "Please enter exactly 10 digits."

phone_number = input("Enter a 11 digits P.K phone number in any format: ")

# cleaned_number = phone_number.strip().replace("-", " ").replace("(", " ").replace(")", " ").replace(".", " ")

cleaned_number = phone_number.strip()
for char in ["-", "(", ")", "."]:
    cleaned_number = cleaned_number.replace(char, " ")
chunks = cleaned_number.split()
digits = ''.join(chunks)

if len(digits) == 11 and digits.startswith('0'):
    formatted_number = f" +92({digits[1:4]}){digits[4:7]}-{digits[7:]}"
    print(f"Formatted Phone Number: {formatted_number}")
else:
    print("Please enter exactly 11 digits starting with 0.")