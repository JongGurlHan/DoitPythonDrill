f1 = open("test.txt", 'w')
f1.write("Life is too short")

f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

with open("test.txt", 'a') as f1:
    f1.write(" this is test sentence")

with open("test.txt" , 'r') as f2:
    print(f2.read())