with open("test.txt", 'r')as f:
    a = f.read()
a = a.replace("java", "python")
with open("test.txt", 'w')as f:
    f.write(a)