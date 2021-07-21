# Q5 
# q1
# Calculator 클래스를 상속하는 UpgradeCalculator를 만들고 값을 뺄 수 있는 minus 메서드를 추가해 보자. 즉 다음과 같이 동작하는 클래스를 만들어야 한다.
# class Calculator:
#     def __init__(self):
#         self.value = 0
#     def add(self, val):
#         self.value += val

# class UpgradeCalculator(Calculator):
#     def minus(self, val):
#         self.value -= val

# cal = UpgradeCalculator()
# cal.add(10)
# cal.minus(7)

# print(cal.value)

# q2
# 객체변수 value가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어 보자. 즉 다음과 같이 동작해야 한다.
# class Calculator:
#     def __init__(self):
#         self.value = 0

#     def add(self, val):
#         self.value += val

# class MaxLimitCalculator(Calculator):
#     def add(self, val):
#         self.value += val
#         if self.value > 100:
#             self.value = 100

# cal = MaxLimitCalculator()
# cal.add(50)
# cal.add(20)

# print(cal.value)

# q3
# 다음 결과를 예측해 보자.
# print(all([1, 2, abs(-3)-3]))
# # False 
# print(chr(ord('a')) == 'a')
# # True

# q4
# filter와 lambda를 사용하여 리스트 [1, -2, 3, -5, 8, -3]에서 음수를 모두 제거해 보자.
# print(list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3])))

# q5
# 234라는 10진수의 16진수는 다음과 같이 구할 수 있다.
# print(int(hex(234), 16))

# q6
# map과 lambda를 사용하여 [1, 2, 3, 4] 리스트의 각 요솟값에 3이 곱해진 리스트 [3, 6, 9, 12]를 만들어 보자.
# print(list(map(lambda x: x * 3, [1, 2, 3, 4])))

# q7
# 다음 리스트의 최댓값과 최솟값의 합을 구해 보자.
# num = [-8, 2, 7, 5, -3, 5, 0, 1]
# print(max(num) + min(num))

# q8
# 17 / 3의 결과는 다음과 같다.
# print(round(17 / 3, 4))

# q9
# 다음과 같이 실행할 때 입력값을 모두 더하여 출력하는 스크립트(C:\doit\myargv.py)를 작성해 보자.
# import sys
# print(sum(list(map(int, sys.argv[1:]))))

# q10
# os 모듈을 사용하여 다음과 같이 동작하도록 코드를 작성해 보자. 
# list를 string로 만들어주는 join 함수는 split의 reverse function으로 볼수있다
# import os
# ls_home = os.popen('ls ~/')
# print(' '.join(ls_home.read().split()))

# q11
# glob 모듈을 사용하여 C:\doit 디렉터리의 파일 중 확장자가 .py인 파일만 출력하는 프로그램을 작성해 보자.
# import glob
# print(glob.glob('/Users/kkkk/jong-jung/python/jump_to_python/doit/*.py'))
# home directory 경로 찾기
# import os.path
# print(os.path.expanduser('~'))

# q12
# time 모듈을 사용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력해 보자.
# import time
# list = list(map(str,(time.localtime(time.time()))))
# year_month_day = "/".join(list[0:3])
# hour_minute_second = ":".join(list[3:6])
# print(year_month_day + " %s" % hour_minute_second)

# print(time.strftime("%Y/%m/%d %H:%M:%S"))
# print(time.strftime("%Y/%m/%d %X"))

# q13
# random 모듈을 사용하여 로또 번호(1~45 사이의 숫자 6개)를 
# 생성해 보자(단 중복된 숫자가 있으면 안 됨).
# import random
# num = [i for i in range(1, 46)]
# random.shuffle(num)
# for idx, val in enumerate(num):
#     if idx < 6:
#         print(num.pop())

# list로 출력
# import random
# result = []
# while len(result) < 6:
#     num = random.randint(1,45)
#     if num not in result:
#         result.append(num)
# print(result)