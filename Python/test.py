from typing import List


N, M = map(int, input().split())
l = [[ord(val) + idx + i & 1 for idx, val in enumerate(input())]for i in range(N)]
# print(min(32-abs(sum(4-sum(l[j:j+8])for l in list[i:i+8]))for i in range(N-7)for j in range(M-7)))

print([[l[j:j+8] for l in l[i:i+8]]for i in range(N-7)for j in range(M-7)])
# for n in range(N-7):
#     for m in range(M-7):
#         count1 = 0
#         count2 = 0
#         for a in range(n, n+8):
#             for b in range(m, m+8):
#                 if (a+b) % 2 == 0:
#                     if list[a][b] == "W":
#                         count1 += 1
#                     elif list[a][b] == "B":
#                         count2 += 1
#                 if (a+b) % 2 != 0:
#                     if list[a][b] == "B":
#                         count1 += 1
#                     elif list[a][b] == "W":
#                         count2 += 1
#         result.append(min(count1, count2))
# print(min(result))  W = 87, B = 98