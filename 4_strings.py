msg = "Hello! Welcome to Python 101 course"

# Message printing
print(msg)
print(msg + msg)
print(msg , msg)
print(msg * 4)

# String methods
print(msg.upper())
print(msg.lower())
print(msg.capitalize())
print(msg.title())

# String indexing
print(len(msg))
print(msg.count("y"))

# Slicing
print(msg[2])
print(msg[10:14])
print(msg[:6])
print(msg[-2])


print(msg.find("101"))
replace = msg.replace("Python", "Javascript")  
print(replace)
print("Javascript" not in msg)
print("Python" in replace)