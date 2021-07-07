def average(*args):
    n = 0
    for i in args:
        n += i
    return n
l = list(map(int, input().split()))
print(average(*l))