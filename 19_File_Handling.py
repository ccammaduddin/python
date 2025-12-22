# my_file = open('greeting.txt','r') #w, a
# print(my_file.read(10))
# print(my_file.readline())
# print(my_file.readline())
# line_by_line = my_file.readlines()
# line_by_line1 = my_file.read().splitlines()
# print('readlines: ',line_by_line)
# print('splitlines: ',line_by_line1)
# my_file.close()


# with open('friends.csv','r') as f:
#     friends = f.read().splitlines()
#     print(friends)
#     for friend in friends:
#         friend = friend.split(',')
#         name = friend[0]
#         year = int(friend[1].strip())
#         print(f'In 2030 {name} will be {2030 -year} years old')


with open('movies.txt','r') as f:
    for line in f:
        print(line)