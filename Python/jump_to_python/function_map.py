# def two_times(numberList):
#     result = []
#     for number in numberList:
#         result.append(number * 2)
#     return result

# result = two_times([1, 2, 3, 4])
# print(result)

def two_times(x):
    return x * 2

# 리스트의 요소가 순차적으로 two_times의 입력값으로 들어간다.
print(list(map(two_times, [1, 2, 3, 4])))

# lambda 사용으로 더간략하게 만들수 있다.
print(list(map(lambda a: a*2, [1, 2, 3, 4])))