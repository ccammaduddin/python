def separator():
    print("..............................................")

for i in range(2,21,2): # start, end, step
    print(i)

separator()

friends_names = ["Ammad", "Najaf", "Hasnain", "Sahad", "Mudassir"]
for index in range (len(friends_names)): # get the length of array
    if friends_names[index] == "Hasnain": #chek if at the index friend name is hasnain
        print("Found " + friends_names[index] + "!") 
        break # break the loop
    print(friends_names[index]) # gets the friend name at the index, friend_names[1] will get the second element of the array

separator()

for name in friends_names:
    if name == "Sahad":
        print("Found " + name + "!")
        continue # skip the current iteration
    print(name)

separator()

for friend in friends_names:
    for number in range(1, 4):
        print(friend, number)