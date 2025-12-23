import random, string

smallcaps = 'abcdefghijklmnopqrstuvwxyz'
largecaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'

def space(): print("-----------------------")

for i in range(5):
    res = random.uniform(1,6)
    print(res)
space()

for i in range(5):
    print(random.randint(1,6))
space()

for i in range(5):
    print(random.randrange(1,100,2))
space()

friends_list =  ['John', 'Eric', 'Michael', 'Terry', 'Graham']
print(random.sample(friends_list,5))
random.shuffle(friends_list)
print(friends_list)

space()

letters_numbers = string.ascii_letters + string.digits
word = ''

for i in range(7):
    word += random.choice(letters_numbers)

word1 = ''.join(random.sample(letters_numbers,7))
word = random.choices(letters_numbers, k=7)    

print(word)
space()
print(word1)