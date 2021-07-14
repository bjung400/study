'''
def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result
'''
def positive(x):
    return x > 0
    
print(list(filter(positive, [1, -0, 2, -5, 3])))

# lambda식 활용
print(list(filter(lambda x: x > 0, [1, -0, 2, -5, 3])))