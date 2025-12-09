is_raining = True
is_cold = True
print("Good Morning!")
if is_raining and is_cold: 
    print("Bring umbrella and jacket!")
elif is_raining and not(is_cold):
    print("Bring umbrella!")
elif not(is_raining) and is_cold:
    print("Bring jacket!")
else:
    print("Its a nice day!")