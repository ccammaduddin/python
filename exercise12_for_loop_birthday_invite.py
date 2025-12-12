names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
names2 = []

msg = "you are cordially invited to my birthday party!"

# my solution

# while True:
#     new_name = input("Enter a friend name to invite (or type 'done' to finish): ")
#     if (new_name.lower() == "done"):
#         break
#     names2.append(new_name)

# friends_list = names + names1 + names2

# for name in friends_list:
#     print(f"Dear {name.title()}! {msg}")


# teacher solution

names.extend(names1)

for index in range(2):
    names.append(input('Enter a new name: '))

for name in names:
    msg1 = f'{name.title()}! {msg}'
    print(msg1)