msg='welcome to Python 101: Strings'
tyler = msg[-6] + msg[12] + msg[2] + msg[1] + msg[-5]
new_msg = msg[18] + " " + msg[0:7] + " " + msg[-5:-1] + " " + msg[8:10] + " " + tyler
# 1 Welcome Ring To Tyler
print(new_msg.title())

# Reversed String
# Relyt Ot Gnir Emoclew 1
print(new_msg[::-1].title())