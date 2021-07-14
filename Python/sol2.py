def solution(s, n):
    arr = [0]*len(s)
    a = 0
    str = ''
    for i in s:
        arr[a] = ord(i)
    
        arr[a] += n
        if arr[a] > 122:
            arr[a] = 97
        
        arr[a] = chr(arr[a])
        a += 1

    print(''.join(arr))
    answer = ''.join(arr)
    return answer
solution("z  b", 1)