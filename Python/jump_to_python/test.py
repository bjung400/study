# q1 문자열 바꾸기
# str = "a:b:c:d"
# print('#'.join(str.split(':')))

# q2 딕셔너리 값 추출하기
# get 함수를 사용하면 해당 key가 없을 경우에는 두번째 매개변수로 전달된 default 값을 대신 돌려준다.
# a = {'A':90, 'B':80}
# print(a.get('C', 70))

# q3 리스트의 더하기와 extend 함수
# a = [1, 2, 3]
# a = a + [4, 5]
# print(a)

# a = [1, 2, 3]
# a = a + [4, 5]
# a.extend([4, 5]) # 리스트 끝에 iterable의 모든 항목을 넣습니다.
# print(id(a))
# q4 리스트의 총합 구하기
# A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
# print(sum([i for i in A if i >= 50]))

# q5 피보나치 함수
# def Fibonacci(n):
#     list = [0, 1]
#     idx = 0
#     while(True):
#         list.append(list[idx] + list[idx + 1])
#         idx += 1
#         if list[-1] == n:
#             return list
#         elif list[-1] > n:
#             list.pop(-1)
#             return list
# def fib(n):
#     if n == 0 : return 0          # n이 0일 때는 0을 반환
#     if n == 1 : return 1          # n이 1일 때는 1을 반환
#     return fib(n-2) + fib(n-1)    # n이 2 이상일 때는 그 이전의 두 값을 더하여 반환

# for i in range(100):
#     print(fib(i))

# print(Fibonacci(4))

# q6 숫자의 총합 구하기
# num = input("숫자 입력 : ")
# num = num.split(',')
# print(sum(list(map(int,num))))

# q7 한 줄 구구단
# num = int(input("구구단을 출력할 숫자를 입력하세요 : "))
# print([num * i for i in range(1, 10)])
# for i in range(1, 10):
#     print("%d" % (num * i),end = ' ')

# q8 역순 저장
# f = open("abc.txt", 'r')
# lines = f.readlines()
# f.close()

# lines.reverse()

# f = open("abc.txt", "w")
# for line in lines:
#     line = line.strip()
#     f.write(line)
#     f.write('\n')
# f.close()

# q9 평균값 구하기
# f = open("sample.txt", 'w')
# f.write("""\
# 70
# 60
# 55
# 75
# 95
# 90
# 80
# 80
# 85
# 100""")
# f.close()
# f = open("sample.txt", 'r')
# lines = f.readlines()
# f.close()

# sum = 0
# for line in lines:
#     score = int(line)
#     sum += score
# average = sum / len(lines) 

# f = open("result.txt", 'w')
# f.write(str(average))
# f.close()

# q10 사칙연산 계산기
# class Calculator:
#     def __init__(self, list):
#         self.result = list

#     def sum(self):
#         return sum(self.result)
        
#     def average(self):
#         return sum(self.result) / len(self.result)


# cal1 = Calculator([1,2,3,4,5])
# print(cal1.sum())
# print(cal1.average())

# cal2 = Calculator([6,7,8,9,10])
# print(cal2.sum())
# print(cal2.average())
        
# q11 모듈 사용 방법
# 1. sys module 사용
# import sys
# sys.path.append("/Users/bjung/bjung_temp/Python/jump_to_python/doit")
# import mymod
# 2 PYTHONPATH 환경 변수 사용
# 3 현재 directory 사용

# q12 오류와 예외 처리
# result = 0

# try:
#     [1, 2, 3][3] # IndexError
#     "a"+1 # TypeError
#     7 / 0 # ZeroDivisionError 
# except TypeError:
#     result += 1
# except ZeroDivisionError:
#     result += 2
# except IndexError:
#     result += 3
# finally:
#     result += 4

# print(result)

# q13 Dashinsert
# def Dashinsert(number):
#     result = []
#     data = number
#     num = list(map(int, data))
#     for i, n in enumerate(num):
#         result.append(str(n))
#         if i < len(num)-1:
#             odd = n % 2 != 0
#             next_odd = num[i+1] % 2 != 0

#             if odd and next_odd: result.append('-')
#             elif not odd and not next_odd: result.append('*')
#     return ''.join(result)

# print(Dashinsert("4546793"))

# q14 문자열 압축하기
# def compress_string(data):
#     result = []
#     count = 1
#     for i, s in enumerate(data):
#         if i < len(data)-1:
#             if s == data[i+1]:
#                 count += 1
#             elif s != data[i+1]:
#                 result.append(s)
#                 result.append(str(count))
#                 count = 1
#         else:
#             result.append(s)
#             result.append(str(count))
#     return ''.join(result)

# def compress_string(s):
#     _c = ""
#     cnt = 0
#     result = ""
#     for c in s:
#         if c != _c: # check
#             _c = c 
#             if cnt: result += str(cnt) #character count add
#             result += c
#             cnt = 1 #count reset
#         else: # c == _c: cnt += 1
#             cnt += 1
#     if cnt: result += str(cnt)
#     return result       
        
# print(compress_string("aaabbcccccca"))
# q15 Duplicate Numbers
# def dup_number(number):
#     result = ""
#     for i in number:
#         if i not in result:
#             result += (i)
#         else: return False
#     return len(result) == 10
    
# print(dup_number("012322456789"))

# q16 모스 부호 해독
dic = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z'
}

# def morse(src):
#     result = []
#     for i, word in enumerate(src.split("  ")):
#         for char in word.split(' '):
#             result.append(dic[char])
#         print(i)
#         result.append(" ")

#     return ''.join(result)

# print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))

reverse_dict = dict(map(reversed, dic.items()))

def morse(src):
    result = []
    for i, word in enumerate(src):
        if word in reverse_dict.keys():
            result.append(reverse_dict[word])
        result.append(' ')
    return ''.join(result)

print(morse("SEND MONEY"))
    
        
        

            
            