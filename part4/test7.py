f = open('test.txt', 'r')
body = "Life is too short \n You need java"
f.close

body = body.replace("java", "python")

f = open('test.txt', 'w')
f.write(body)
f.close()