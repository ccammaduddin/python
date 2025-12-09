msg ='Welcome    to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(msg.split())
print(csv.split(','))
print(' | '.join(csv.split(',')))
print(' , '.join(friends_list))