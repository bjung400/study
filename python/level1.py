def solution(strings, n):
    arr = [0]*len(strings)
    a = 0
    dic = {}

    for i in range(len(strings)):
        dic[i] = (strings[a][n])
        arr[i] = strings[a][n]
        a += 1
        
                  
    # for i in range(len(dic)):
    #     for j in range(len(dic)-1):
    #         if dic[j] > dic[j+1]:
    #             dic[j], dic[j+1] = dic[j+1], dic[j]

    for i in range(len(arr)):
        print(dic[i])

    answer = dic
    return answer
arr = ["sun", "bed", "car"]
print(solution(arr, 1))
if 'a' < 'b':
    print("test")
