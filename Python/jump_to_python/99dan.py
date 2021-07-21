def GuGu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n * i)
        i = i + 1
    return result

def GuGu(n):
    result = [i * n for i in range(1, 10)]
    return result

def GuGu(n):
    return list(map(lambda x: x*n, range(1,10)))

# 99단 전체 출력
list = [i for i in range(2, 10)]
for idx, val in enumerate(list):
    print("%d단 :" % (idx+2), GuGu(val))