def nextMoney(x, day):
    for i in range(day):
        x += (x * 0.02)
    return x

x = 1000000000

print("손실 : %d" % (x * 0.09))
x = x - (x * 0.09)

print(nextMoney(x, 4))