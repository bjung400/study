average = {'국어':80, '영어':75, "수학":55}
num = list(average.values())
i = 0
sum = 0
while i < len(num):
    sum = sum + num[i]
    i = i + 1
print(sum / len(num))