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
# string = 'abcdfe2a354a32a'
# result = string.replace('a', 'A')
# print(result)

# 030 replace 메서드
# 문자열은 immutable한 자료형이므로 그대로 출력된다.
# replace 메서드를 사용하면 원본은 그대로 둔채 변경된 새로운 문자열 객체를 Return해준다.
# string = 'abcd'
# string.replace('b', 'B')
# print(string)

# 031 문자열 합치기
# 문자열에 대한 덧셈은 문자열의 연결을 의미한다.
# 따라서 "34"라는 새로운 문자열이 생성되고 print함수에 의해 출력된다.
# a = "3"
# b = "4"
# print(a+b)

# 032 문자열 곱하기
# 문자열에 대한 곱셉은 문자열의 반복을 의미한다.
# print("Hi"*3)

# 033 문자열 곱하기
# print('-'*80)

# 034 문자열 곱하기
# t1 = 'python'
# t2 = 'jave'
# t3 = t1+' '+t2+' '
# print(t3*4)

# 035 문자열 출력(% formatting을 사용할때)
# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print("이름 : %s 나이 : %d" % (name1, age1))
# print("이름 : %s 나이 : %d" % (name2, age2))

# 036 문자열 출력(문자열의 format() 메서드를 사용할때)
# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print("이름 : {} 나이 : {}".format(name1, age1))
# print("이름 : {} 나이 : {}".format(name2, age2))

# 037 문자열 출력
# %-formatting 이나 str.format()보다 훨씬 직관적으로 사용가능하다
# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print(f"이름 : {name1} 나이 : {age1}")
# print(f"이름 : {name2} 나이 : {age2}")

# 038 컴마 제거하기
# replace로 comma제거후 int()함수로 정수로 변환
# 상장주식수 = "5,969,782,550"
# comma_remove = 상장주식수.replace(',','')
# type_changed = int(comma_remove)
# print(type_changed, type(type_changed))

# 039 문자열 슬라이싱
# 분기 = "2020/03(E) (IFRS연결)"
# print(분기[:7])

# 040 strip 메서드
# strip() 메서드는 문자열에서 좌우 공백을 제거해주고 
# 새로운 문자열이 반환됩니다.
# data = "    w삼성전자   "
# result = data.strip().strip('w')
# print(result)

