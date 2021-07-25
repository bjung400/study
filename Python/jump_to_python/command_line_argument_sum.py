import sys
#명령 라인 인자의 숫자들을 하나씩 다더해주는 함수 
print(sum(list(map(int,([j for i in sys.argv[1:] for j in i])))))