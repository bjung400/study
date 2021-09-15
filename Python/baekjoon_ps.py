# 2920
# music = input().split()
    
# ascending = [i for i in range(1, 9)]

# music = list(map(int, music))

# if music == ascending: print("ascending")
# elif music == ascending[::-1]: print("descending")
# else: print("mixed")

# 2475
# # n = list(map(int, input().split()))

# print(sum(int(n)*int(n) for n in input()[::2]) % 10)

# 2908
# # print(sorted(input()[::-1].split(), reverse=True)[0])
# print(max(input()[::-1].split()))

# 1018
# N, M = map(int, input().split())
# original = []
# count = []

# [original.append(input()) for i in range(N)]

# for a in range(N-7):
#     for b in range(M-7):
#         index1 = 0
#         index2 = 0

#         for i in range(a, a+8):
#             for j in range(b, b+8):
#                 if (i+j) % 2 == 0:
#                     if original[i][j] != 'W':
#                         index1 += 1
#                     if original[i][j] != 'B':
#                         index2 += 1
#                 else:
#                     if original[i][j] != 'B':
#                         index1 += 1
#                     if original[i][j] != 'W':
#                         index2 += 1
#         count.append(min(index1, index2))

# count.append(min(index1, index2))

# print(min(count))
        

# example = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"]
# example_2 = ["BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"]

N, M = map(int, input().split())

original = []
count = []

[original.append(input()) for _ in range(N)]

for a in range(N - 7):
    for b in range(M - 7):
        check1 = 0
        check2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if original[i][j] == 'W':
                        check1 += 1
                    if original[i][j] == 'B':
                        check2 += 1
                else:
                    if original[i][j] == 'B':
                        check1 += 1
                    if original[i][j] == 'W':
                        check2 += 1
        
            
                    

