print('Guessing game') 
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)

i=1
while i<=10:
    input_value = input(f"Enter your guess (1-100) (Attempt {i}/10): ")
    user_guess = int(input_value)
    correct_number = 42
    if user_guess >= 1 and user_guess <= 100:
        if user_guess < correct_number:
            print(f"Your guess ({user_guess}) is too low.")
        elif user_guess > correct_number:
            print(f"Your guess ({user_guess}) is too high.")
        else:
            print("Congratulations! You've guessed the correct number.")
            break
    else:
        print("Enter Valid Number between 1-100")
    i += 1 
    if i > 10:
        print(f"Sorry, you've used all your attempts. The correct number was {correct_number}.")