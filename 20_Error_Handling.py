lowest_limit = 1
highest_limit = 10
fact = 1
try:
    # Code that might cause an error
    # Runs FIRST, always
    num = int(input(f"Enter a valid number between {lowest_limit} and {highest_limit} : "))
    if num > highest_limit:
        raise ValueError(f"The number {num} is greater than {highest_limit}")
except ZeroDivisionError as err:
    # Runs ONLY if an error occurs in try block
    # Handles the error
    print(err, " :  You cannot divide by zero")
except Exception as err:
    print("An error occurred:", err)
else:
    # Runs ONLY if NO error occurred in try block
    # Executes after try, before finally
    for i in range(0, num):
        fact = fact*(num-i)
        i+=1
    print(f"The factorial of {num} is {fact}")
finally:
    # ALWAYS runs, no matter what
    # Runs whether error occurred or not
    print("Execution completed.")