# 01. 파이썬 시작하기
# 001 print 기초
# print("Hello World")

# 002 print 기초
# print("Mary's cosmetics")

# 003 print 기초
# print('신씨가 소리질렀다. "도둑이야".')

# 004 print 기초
# print("C:\Windows")

# 005 print 탭과 줄바꿈
# print("안녕하세요.\n만나서\t\t반갑습니다.")

# 006 print 여러 데이터 출력
# print("오늘은", "일요일")

# 007 print 기초
# print("naver","kakao","samsung", sep=";")

# 008 print 기초
# print("naver","kakao","sk","samsung", sep='/')

# 009 print 줄바꿈
# print("first", end="");print("second")

# 010 연산 결과 출력
# print(5/3)

# 02. 파이썬 변수
# 011 변수 사용하기
# 삼성전자 = 50000
# 총평가금액 = 삼성전자*10
# print(총평가금액)

# 012 변수 사용하기
# 시가총액 = 298000000000000
# 현재가 = 50000
# PER = 15.7
# print(시가총액, type(시가총액))
# print(현재가, type(현재가))
# print(PER, type(PER))

# 013 문자열 출력
# s = "hello"
# t = "python"
# print("%s! %s"% (s, t))
# print(s+'!', t)

# 014 파이썬을 이용한 값 계산
# print(2+2*3)

# 015 type 함수
# a = 132
# print(type(a))

# 016 문자열을 정수로 변환
# num_str = "720"
# num_int = int(num_str)
# print(num_int+1, type(num_int))

# 017 정수를 문자열 100으로 변환
# num = 100
# result = str(num)
# print(result, type(result))

# 018 문자열을 실수로 변환
# data = "15.79"
# result = float(data)
# print(result, type(result))

# 019 문자열을 정수로 변환
# year = "2020"
# year = int(year)-3
# for i in range(3):
#     print(year+i)

# 020 파이썬 계산(Air Conditioner Price)
# month = 48584
# all_price = 48584*36
# print(all_price, '원', sep='')

# 03. 파이썬 문자열
# 021 문자열 인덱싱
# letters = 'python'
# print(letters[0], letters[2])

# 022 문자열 슬라이싱
# license_plate = "24가 2210"
# print(license_plate[4:])
# print(license_plate[-4:])

# 023 문자열 인덱싱
# string = "홀짝홀짝홀짝"
# print(string[::2])

# 슬라이싱할 때 시작인덱스:끝인덱스:오프셋을 지정가능
# 024 문자열 슬라이싱
# string = "PYTHON"
# print(string[::-1])

# 025 문자열 치환 문자열은 수정할 수 없는 자료형이므로 기존 문자열은 그대로 두고 치환된 새로운 문자열이 리턴됩니다.
# phone_number = "010-1111-2222"
# result = phone_number.replace('-',' ')
# print(result)

# 026 문자열 다루기
# phone_number = "010-1111-2222"
# result = phone_number.replace('-','')
# print(result)

# 027 문자열 다루기
# url ="http://sharebook.kr"
# print(url[-2:])
# url_split = url.split('.')
# print(url_split[1])

# 028 문자열은 immutable
# TypeError: 'str' object does not support item assignment
# 문자열은 수정할수없다, 할당(assignment) 메서드를 지원하지 않는다.
# lang = "python"
# lang[0] = 'P'
# print(lang)

# 029 replace 메서드
string = 'abcdfe2a354a32a'
result = 'A'+string[1:]
print(result)