def greet(name, age=20):
    # print("Hello " + name + ", you are " + str(age) + "!") #We have to convert number to string with this methdod
    print(f"Hello {name}, you are {age}!") # here we do not need to convert number to string, it works anyway

name = input("Enter your first name: ")
age = input("Enter your age: ")
greet(name, age)