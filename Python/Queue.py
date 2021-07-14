def solution(mylist):
    answer = []
    n = 0
    for i in mylist:
        if n <= len(mylist)-2:
            answer.append(mylist[n] - mylist[n+1])
            if answer[n] < 0:
                answer[n] = abs(answer[n])

        n += 1
    print(len(mylist))
    return answer
print(solution([83, 48, 13, 4, 71, 11]))