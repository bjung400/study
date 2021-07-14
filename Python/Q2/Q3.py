i = 1
while i <= 5:
    j = 0
    while(j < i):
        print("*", end = "")
        j += 1
    print('')
    i += 1
i = 0
while True:
    i += 1
    if i > 5: break
    print('*' * i)