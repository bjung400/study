# # list comprehension
# def solution(a, b):    
#     ansewr = sum([x for x in range(max(a,b)) if x > min(a,b)])
#     return ansewr + a + b
# print(solution(1,4))

# # 하샤드 수
# def solution(x):
#     a = []
#     for i in str(x):
#         a.append(i)
#     a = list(map(int,a))
#     if x % sum(a) == 0: answer = True
#     else: answer = False
#     return answer
# print(solution(11))

# # 체육복 분실
# def solution(n, lost, reserve):
#     answer = 0
#     a = 0
#     lost_check = [1] * len(lost)
#     for i in lost:
#         for j in reserve:
#             if lost_check[a] == 1 and i+1 == j or i-1 == j:
#                 answer += 1
#                 lost_check[a] = 0
#                 print("i = %d, j = %d answer ++" % (i,j))
#         a += 1
#     return (n - len(lost)) + answer 
# print(solution(3,[3],[1]))

# # 로또
# def solution(lottos, win_nums):
#     max, min = 0, 0
    
#     for i in lottos:
#         if i == 0: max += 1
#         for j in win_nums:
#             if i == j:
#                 max += 1
#                 min += 1
    
#     if max == 2: max = 5
#     elif max == 3: max = 4
#     elif max == 4: max = 3
#     elif max == 5: max = 2
#     elif max == 6: max = 1
#     else: max = 6
    
#     if min == 2: min = 5
#     elif min == 3: min = 4
#     elif min == 4: min = 3
#     elif min == 5: min = 2
#     elif min == 6: min = 1
#     else: min = 6
#     answer = []
#     answer.append(max)
#     answer.append(min)
#     return answer
# print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))

# #배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.
# def solution(array, commands):
#     answer = []
#     for command in commands:
#         i, j, k = command[0], command[1], command[2]
#         slice = array[i-1:j]
#         slice.sort()
#         answer.append(slice[k-1])
#     return answer
# print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

#문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수
# def solution(s):
#     # a = [ord(i) for i in s]
#     # a.reverse()
#     # a = [chr(i) for i in a]
#     # a = "".join(a)
#     s = list(s)
#     return "".join(sorted(s, reverse=True))
#     return s
# print(solution("Zbcdefg"))

#정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.
# def solution(arr):
#     average = 0
#     for i in arr:
#         average += i
#     average = average / len(arr)
#     answer = average
#     return answer
# print(solution([1,2,3,4]))

#로또 6/45(이하 '로또'로 표기)는 1부터 45까지의 숫자 중 6개를 찍어서 맞히는 대표적인 복권입니다. 아래는 로또의 순위를 정하는 방식입니다. 1
# def solution(lottos, win_nums):
#     min = [i for i in lottos for y in win_nums if i == y]
#     max = [i for i in lottos if i == 0]
#     min = len(min)
#     max = min + len(max)

#     if max == 2: max = 5
#     elif max == 3: max = 4
#     elif max == 4: max = 3
#     elif max == 5: max = 2
#     elif max == 6: max = 1
#     else: max = 6

#     if min == 2: min = 5
#     elif min == 3: min = 4
#     elif min == 4: min = 3
#     elif min == 5: min = 2
#     elif min == 6: min = 1
#     else: min = 6

#     answer = []
#     answer.append(max)
#     answer.append(min)
#     return answer
# print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))

# #정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.
# def solution(arr):
#     average = sum([i for i in arr]) / len(arr)
#     return average
# print(solution([1,2,3,4]))

#JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 
# 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.
# def solution(s):
#     answer = []
#     count = 0

#     for i in s:
#         i = ord(i)
#         if i >= 65 and i <= 90 and count == 1:
#             i += 32
#         if i != 32 and count == 0:
#             if i >= 97 and i <= 122:
#                 i -= 32
#             count += 1
#         elif i == 32 and count == 1:
#             count -= 1
#         i = chr(i)
#         answer.append(i)

#     return ''.join(answer)
# print(solution("3people unFollowed me"))

#ROR
from collections import deque

def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    r = len(maps)
    c = len(maps[0])

    graph = [[-1 for _ in range(c)] for _ in range(r)]

    queue = deque()
    queue.append([0, 0])

    graph[0][0] = 1

    while queue:
        print(queue)
        y, x = queue.popleft()
        print(y, x)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < r and 0 <= nx < c and maps[ny][nx] == 1:
                if graph[ny][nx] == -1:
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append([ny,nx])
    answer = graph[-1][-1]
    return answer
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))