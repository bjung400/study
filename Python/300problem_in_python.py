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
# print(!"% (s, t))
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
# print("이름 : 나이 : %d" % (name1, age1))
# print("이름 : 나이 : %d" % (name2, age2))

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

# 041 upper 메서드
# upper 메서드를 호출하면 대문자로 문자열 객체가 반환된다
# 반환된 새로운 객체는 새로운 변수에 바인딩해야 한다
# ticker = "btc_krw"
# result = ticker.upper()
# print(result)

# 042 lower 메서드
# ticker = "BTC_KRW"
# result = ticker.lower()
# print(result)

# 043 capitalize 메서드
# a = "hello"
# result = a.capitalize()
# print(result)

# 044 endswith 메서드
# file_name = "보고서.xlsx"
# result = file_name.endswith(".xlsx")
# print(result)

# 045 endswith 메서드
# 정의된 문자열이 지정된 접미사로 끝나면 True를 돌려준다.
# file_name = "보고서.xlsx"
# result = file_name.endswith(("xls", "sx"))
# print(result)

# 046 startswith 메서드
# 정의된 문자열이 지정된 접두사로 시작하면 True를 돌려준다.
# file_name = "2020_보고서.xlsx"
# result = file_name.startswith("2020")
# print(result)

# 047 split 메서드
# a = "hello world"
# result = a.split()
# print(result)

# 048 split 메서드
# ticker = "btc_krw"
# result = ticker.split('_')
# print(result)

# 049 split 메서드
# date = "2020-05-01"
# result = date.split('-')
# print(result)

# 050 rstrip 메서드
# rstrip() 메서드를 사용하면 오른쪽 공백이 제거된
# 새로운 문자열 객체가 반환된다 그값을 result 변수가 새로 바인딩한다.
# data = "039490     "
# result = data.rstrip()
# print(result)

# 04. 파이썬 리스트 
# 파이선 리스트는 순서가 있고 수정 가능한 자료구조입니다.

# 051 리스트 생성
# movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
# print(movie_rank)

# 052 리스트에 원소 추가
# movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
# movie_rank.append("배트맨")
# print(movie_rank)

# 053 리스트의 insert() 메서드를 사용하면 특정위치에 값을 끼어넣을수있다
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# movie_rank.insert(1, "슈퍼맨")
# print(movie_rank)

# 054 movie_rank 리스트에서 '럭키'를 삭제하라.
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
# # movie_rank.remove("럭키")
# del movie_rank[3]
# print(movie_rank)

# 055 movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
# del movie_rank[2]
# del movie_rank[2]
# print(movie_rank)

# 056 lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
# lang1 = ["C", "C++", "JAVA"]
# lang2 = ["Python", "Go", "C#"]
# result = lang1+lang2
# print(result)

# 057 다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)
# nums = [1, 2, 3, 4, 5, 6, 7]
# max = max(nums)
# min = min(nums)
# print(f"max : {max}")
# print(f"min : {min}")

# 058 다음 리스트의 합을 출력하라.
# nums = [1, 2, 3, 4, 5]
# print(sum(nums))

# 059 다음 리스트에 저장된 데이터의 개수를 화면에 구하라.
# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
# print(len(cook))

# 060 다음 리스트의 평균을 출력하라.
# nums = [1, 2, 3, 4, 5]
# average = sum(nums)/len(nums)
# print(average)

# 061 price 변수에는 날짜와 종가 정보가 저장돼 있다. 
# 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)
# price = ['20180728', 100, 130, 140, 150, 160, 170]
# print(price[1:])

# 062 슬라이싱을 사용해서 홀수만 출력하라.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[::2])

# 063 슬라이싱을 사용해서 짝수만 출력하라.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[1::2])

# 064 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
# nums = [1, 2, 3, 4, 5]
# print(nums[::-1])

# 065 interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver']
# print(interest[0], interest[2])

# 066 join 메서드
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print(' '.join(interest))

# 067 join 메서드
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print('/'.join(interest))

# 068 join 메서드
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print('\n'.join(interest))

# 069 문자열 split 메서드
# string = "삼성전자/LG전자/Naver"
# interest = string.split('/')
# print(interest)

# 070 리스트 정렬
# data = [2, 4, 3, 1, 5, 10, 9]
# data.sort() # 원래 변수가 수정, 반환값 : None
# print(data) 
# print(sorted(data)) # 다른 변수에 저장 가능, 반환값 : list 
# key를 통해 원하는 정렬키 설정도 가능
# array = [['a', 1], ['c', 4], ['b', 3], ['d', 2]]
# array.sort(key = lambda x:x[1])
# print(array)
# print(sorted(array, key=lambda x:x[0]))

# 05. 파이썬 튜플
# 파이썬 튜플은 순서가 있지만 수정 불가능한 자료구조입니다.

# 071 my_variable 이름의 비어있는 튜플을 만들라.
# my_variable = ()
# print(type(my_variable))

# 072 영화 제목을 movie_rank 이름의 튜플에 저장하라.
# movie_rank = ("닥터스트레인지", "스플릿", "럭키")
# print(movie_rank)

# 073 숫자 1 이 저장된 튜플을 생성하라.
# my_tuple = (1, ) # 튜플로 하나의 데이터가 저장되는경우 쉼표를 입력해야함
# print(type(my_tuple))

# 074 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
# tuple은 element의 수정이 불가능하다
# t = (1, 2, 3)
# t[0] = 'a'
# print(t)

# 075 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. 
# t가 바인딩하는 데이터 타입은 무엇인가? tuple
# 튜플은 괄호와 함께 데이터를 정의해야 하지만, 사용자 편의를 위해 괄호 없이도 동작합니다.
# t = 1, 2, 3, 4
# print(type(t))

# 076 변수 t에는 아래와 같은 값이 저장되어 있다. 
# 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
# t = ('a', 'b', 'c')
# t = list(t)
# t[0] = 'A'
# print(t)

# 077 다음 튜플을 리스트로 변환하라.
# interest = ('삼성전자', 'LG전자', 'SK Hynix')
# print(list(interest))

# 078 다음 리스트를 튜플로 변경하라.
# interest = ['삼성전자', 'LG전자', 'SK Hynix']
# print(tuple(interest))

# 079 튜플 언팩킹
# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
# print(a, b, c)

# 080 080 range 함수
# range함수는 특정 구간의 숫자의 범위를 만들어주는 함수
# range(a,b,c) a부터 c의간격으로 b-1까지의 정수범위 반환
# data = tuple(range(2, 100, 2))
# print(data)

# 06. 파이썬 딕셔너리
# 파이썬 딕셔너리는 순서는 없지만 key와 value 형태로 데이터를 저장합니다.
# 특히 key는 데이터의 레이블(label)을 지정하는 용도로 자주 사용됩니다.

# 081 별 표현식(star expression)
# 변수의 개수가 달라도 데이터 unpacking을 할수있다
# 좌측 8개 값을 valid_score 변수에 바인딩하는 코드
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# *valid_score, _, _ = scores
# print(valid_score)

# 082 우측 8개의 값을 valid_score 변수에 바인딩
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# _, _, *valid_score = scores
# print(valid_score)

# 083 가운데 8개의 값을 valid_score 변수에 바인딩
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# _, *valid_score, _ = scores
# print(valid_score)

# 084 비어있는 딕셔너리
# temp = {}
# print(type(temp)

# 085 아이스크림 이름과 희망 가격을 딕셔너리로 구성하라.
# ice = {"메로나":1000, "폴라포":1200, "빵파레":1800}
# print(ice)

# 086 085 번의 딕셔너리에 아래 아이스크림 가격정보를 추가하라.
# ice = {"메로나":1000, "폴라포":1200, "빵파레":1800}
# ice['죠스바'] = 1200
# ice['월드콘'] = 1500
# print(ice)

# 087 다음 딕셔너리를 사용하여 메로나 가격을 출력하라.
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}
# print(f"메로나 가격 : {ice['메로나']}")

# 088 다음 딕셔너리에서 메로나의 가격을 1300으로 수정하라.
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}
# ice['메로나'] = 1300
# print(ice['메로나'])

# 089 다음 딕셔너리에서 메로나를 삭제하라.
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}
# del ice['메로나']
# print(ice)

# 090 다음 코드에서 에러가 발생한 원인을 설명하라.
# 딕셔너리에 없는 키를 사용해서 인덱싱하면 에러가 발생
# icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# icecream['누가바']

# 091 딕셔너리 생성
# 아이스크림 이름을 키값으로, (가격, 재고) 리스트를 딕셔너리의 값으로 저장하라.
# inventory = {"메로나":[300, 20],
#              "비비빅":[400, 3],
#              "죠스바":[250, 100]}
# print(inventory)

# 092 딕셔너리 인덱싱
# inventory 딕셔너리에서 메로나의 가격을 화면에 출력하라.
# inventory = {"메로나":[300, 20],
#              "비비빅":[400, 3],
#              "죠스바":[250, 100]}
# print("%d원"% inventory["메로나"][0])

# 093 딕셔너리 인덱싱
# inventory 딕셔너리에서 메로나의 재고를 화면에 출력하라.
# inventory = {"메로나":[300, 20],
#              "비비빅":[400, 3],
#              "죠스바":[250, 100]}
# print("%d개"% inventory["메로나"][1])

# 094 딕셔너리 추가
# inventory 딕셔너리에 아래 데이터를 추가하라.
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
# inventory["월드콘"] = [500, 7]
# print(inventory)

# 095 딕셔너리 keys() 메서드
# 다음의 딕셔너리로부터 key 값으로만 구성된 리스트를 생성하라.
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# l = list(icecream.keys())
# print(l)

# 096 딕셔너리 values() 메서드
# 다음의 딕셔너리에서 values 값으로만 구성된 리스트를 생성하라.
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# l = list(icecream.values())
# print(l)

# 097 딕셔너리 values() 메서드
# icecream 딕셔너리에서 아이스크림 판매 금액의 총합을 출력하라.
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# print(sum(icecream.values()))

# 098 딕셔너리 update 메서드
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# new_product = {'팥빙수':2700, '아맛나':1000}
# icecream.update(new_product)
# print(icecream)

# 099 zip과 dict
# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)
# result = dict(zip(keys, vals))
# print(result)

# 100 zip과 dict
# date = ['09/05', '09/06', '09/07', '09/08', '09/09']
# close_price = [10500, 10300, 10100, 10800, 11000]
# close_table = dict(zip(date, close_price))
# print(close_table)

# 07. 파이썬 분기문
# 파이썬은 if라는 키워드를 통해 분기문을 만들 수 있습니다.

# 101 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가? bool
# result = True
# print(type(result))

# 102 아래 코드의 출력 결과를 예상하라 False
# print(3 == 5)

# 103 아래 코드의 출력 결과를 예상하라 True
# print(3 < 5)

# 104 아래 코드의 결과를 예상하라. True
# x = 4
# print(1 < x < 5)

# 105 아래 코드의 결과를 예상하라. True
# print ((3 == 3) and (4 != 3))

# 106 아래 코드에서 에러가 발생하는 원인에 대해 설명하라.
# 지원하지않는 연산자입니다. 부등호가 먼저들어가야합니다.
# print(3 <= 4)

# 107 아래 코드의 출력 결과를 예상하라 
# 조건을 만족하지 않기 때문에 아무 결과도 출력되지 않습니다.
# if 4 < 3:
#   print("Hello World")

# 108 아래 코드의 출력 결과를 예상하라 Hi, there
# if 4 < 3:
#     print("Hello World.")
# else:
#     print("Hi, there.")

# 109 아래 코드의 출력 결과를 예상하라 1, 2, 4
# if True :
#     print ("1")
#     print ("2")
# else :
#     print("3")
# print("4")

# 110 아래 코드의 출력 결과를 예상하라 3, 5
# if True :
#     if False:
#         print("1")
#         print("2")
#     else:
#         print("3")
# else :
#     print("4")
# print("5")

# 111 사용자로부터 입력받은 문자열을 두 번 출력하라. 
# string = input("입력 : ")
# print(string*2)

# 112 사용자로부터 하나의 숫자를 입력받고, 입력 받은 숫자에 10을 더해 출력하라.
# num = int(input("숫자를 입력하세요 : "))
# print(num+10)

# 113 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.
# num = int(input("숫자를 입력하세요 : "))
# if num % 2 == 0: print("짝수")
# else: print("홀수")

# 114 사용자로부터 값을 입력받은 후 해당 값에 20을 더한 값을 출력하라. 
# 단 사용자가 입력한 값과 20을 더한 계산 값이 255를 초과하는 경우 255를 출력해야 한다.
# num = int(input("입력값 : "))
# if 255 >= num+20: print(f"출력값 : {num+20}")
# else: print(f"출력값 : {255}")

# 115 사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라. 
# 단 출력 값의 범위는 0~255이다. 예를 들어 결괏값이 0보다 작은 값이되는 경우 0을 출력하고 255보다 큰 값이 되는 경우 255를 출력해야 한다.
# num = int(input("입력값 : "))
# num = num-20
# if num > 255: print(255)
# elif num < 0: print(0)
# else: print(num)

# 116 사용자로부터 입력 받은 시간이 정각인지 판별하라.
# t = input("시간 : ")
# if t[3:] == "00": print("정각입니다.")
# else: print("정각이 아닙니다.")

# 117 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라. 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# for문을 사용하지 않고도 in으로 가능
# fruit = ["사과", "포도", "홍시"]
# favorite = input("좋아하는 과일은? ")
# if favorite in fruit: print("정답입니다.")
# else: print("오답입니다.")

# 118 투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 해당 종목이 투자 경고 종목이라면 '투자 경고 종목입니다'를 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# investment = input("종목을 입력하세요 : ")
# if investment in warn_investment_list: print("투자 경고 종목입니다.")
# else: print("투자 경고 종목이 아닙니다.")

# 119 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# favorite_weather = input("제가 좋아하는  계절은 : ")
# if favorite_weather in list(fruit.keys()): print("정답입니다.")
# else: print("오답입니다.")

# 120 아래와 같이 fruit 딕셔너리가 정의되어 있다. 
# 사용자가 입력한 값이 딕셔너리 값 (value)에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# favorite_fruit = input("제가 좋아하는  과일은 : ")
# if favorite_fruit in fruit.values(): print("정답입니다.")
# else: print("오답입니다.")

# 121 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 
# 대문자 일 경우, 소문자로 변경해서 출력하라.
# string = input()
# if string.islower(): print(string.upper())
# else: print(string.lower())

# 122 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score를 입력받아 학점을 출력하라.
# score = int(input("score : "))
# grade = ""
# if 81 <= score <= 100: grade = "A"
# elif 61 <= score <= 80: grade = "B"
# elif 41 <= score <= 60: grade = "C"
# elif 21 <= score <= 40: grade = "D"
# else: grade = "E"
# print(f"grade is {grade}")

# 123 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 
# 이를 원으로 변환하는 프로그램을 작성하라. 각 통화별 환율은 다음과 같다. 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.
# exchange_rate = {
#     # 21.10.16
#     "USD" : 1182,
#     "JPY" : 10.36,
#     "EUR" : 1372,
#     "CNY" : 183.78}
# money, currency = input("입력 : ").split()
# print(f"{float(money)*exchange_rate[currency]}원")

# 124 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
# l = list(int(input(f"input number{i+1} : ")) for i, v in enumerate(range(3)))
# print(max(l))

# 125 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 
# 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.
# carrier = {
#     "011":"SKT",
#     "016":"KT",
#     "019":"LGU",
#     "010":"알수없음"
# }
# n, *_ = input("휴대전화 번호 입력 : ").split('-')
# print(f"당신은 {carrier[n]} 사용자 입니다.")

# 126 우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타낸다. 
# 예를들어, 강북구의 경우 010, 011, 012 세 자리로 시작한다
# 강북구 = ["010", "011", "012"]
# 도봉구 = ["013", "014", "015"]
# 노원구 = ["016", "017", "018", "019"]
# zip_code = input("우편번호 : ")
# if zip_code[:3] in 강북구: print("강북구")
# elif zip_code[:3] in 도봉구: print("도봉구")
# elif zip_code[:3] in 노원구: print("노원구")
# else: print("찾을수 없는 정보입니다.")

# 127 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데, 
# 1, 3은 남자 2, 4는 여자를 의미한다. 사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.
# men = ['1', '3']
# woman = ['2', '4']
# idcard = input("주민등록번호 : ")
# if idcard[-7] in men: print("남자")
# elif idcard[-7] in woman: print("여자")
# else: print("잘못된 정보입니다.")

# 128 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다.
# 주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라
# local = input("주민등록번호 : ").split('-')[1][1:3]
# if 0 <= int(local) <= 8: print("서울입니다")
# else: print("서울이 아닙니다.")

"""129 주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 
   유효성을 체크하는데 사용된다. 먼저 앞에서부터 12자리의 숫자에 
   2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 차례로 곱한 뒤 그 값을 전부 더한다. 
   연산 결과 값을 11로 나누면 나머지가 나오는데 11에서 나머지를 뺀 값이 
   주민등록번호의 마지막 번호가 된다.
"""
# idcard = input("주민등록번호 : ").replace('-','')
# num = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 1]
# l = []
# for i, j in zip(idcard,num):
#     l.append(int(i)*j)
# l.pop()
# if 11-(sum(l)%11) == int(idcard[-1]): print("유효한 주민등록 번호입니다.")
# else: print("유효하지 않은 주민등록 번호입니다.")
'''
130
아래 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다.
btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어있다.
최고가와 최저가의 차이를 변동폭으로 정의할 때
시가 + 변동폭이 최고가 보다 높을 경우 "상승장",
아닌경우 "하락장" 문자열을 출력하라.
'''
# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# change_price = float(btc["min_price"])-float(btc["max_price"]) # 변동폭
# opening_price = float(btc["opening_price"])
# max_price = float(btc["max_price"])

# print(change_price, opening_price, max_price)

# if opening_price+change_price > max_price:
#    print("상승장")
# else:
#    print("하락장")

# 08. 파이썬 반복문
# 파이썬 for 문은 횟수가 정해져 있거나 상대적으로 횟수가 
# 적은 경우에 대한 반복에 주로 사용됩니다. 파이썬 while문은 
# 횟수가 상대적으로 크거나 무한 루프 형태의 반복문에 사용됩니다.

# 131 for문의 실행결과를 예측하라.
# 리스트에 들어있는 문자열이 하나씩 출력된다.
# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#     print(변수)

# 132 for문의 실행결과를 예측하라.
# 리스트의 요소의 개수만큼 print문이 실행된다
# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#   print("#####")

# 133 다음 for 문과 동일한 기능을 수행하는 코드를 작성하세요.
# for 변수 in ["A", "B", "C"]:
#   print(변수)
# "변수 바인딩(라인 1) -> 변수 출력 (라인 2)" 과정을 
# 자료구조 데이터 개수 만큼 반복합니다.
# 변수 = 'A'
# print(변수)
# 변수 = 'B'
# print(변수)
# 변수 = 'C'
# print(변수)

# 134 for문을 풀어서 동일한 동작을하는 코드를 작성하라.
# for 변수 in ["A", "B", "C"]:
#   print("출력 :", 변수)
# 변수 = 'A'
# print("출력 :", 변수)
# 변수 = 'B'
# print("출력 :", 변수)
# 변수 = 'C'
# print("출력 :", 변수)  

# 135 for문을 풀어서 동일한 동작을 하는 코드를 작성하라.
# 들여쓰기된 코드의 실행이 끝나면 라인 1로 이동해서 변수에 두 번째
# 데이터를 바인딩합니다. 그리고 들여쓰기된 코드를 실행합니다.
# for 변수 in ["A", "B", "C"]:
#   b = 변수.lower()
#   print("변환 :", b)

# 변수 = 'A'
# b = 변수.lower()
# print("변환 :", b)
# 변수 = 'B'
# b = 변수.lower()
# print("변환 :", b)
# 변수 = 'C'
# b = 변수.lower()
# print("변환 :", b)

# 136 다음 코드를 for문으로 작성하라.
# 변수 = 10
# print(변수)
# 변수 = 20
# print(변수)
# 변수 = 30
# print(변수)

# l = [10, 20, 30]
# for i in l: print(i)

# 137 다음 코드를 for문으로 작성하라.
# print(10)
# print(20)
# print(30)

# for i in [10, 20, 30]: print(i)

# 138 다음 코드를 for문으로 작성하라.
# print(10)
# print("-------")
# print(20)
# print("-------")
# print(30)
# print("-------")

# for i in [10, 20, 30]: print(i, "-------", sep='\n')

# 139 다음 코드를 for문으로 작성하라.
# print("++++")
# print(10)
# print(20)
# print(30)

# print("++++")
# for i in [10, 20, 30]: print(i)

# if문으로 0번쨰 index일때 ++++출력 
# for i, v in enumerate([10, 20, 30]):
#    if i == 0: print("++++", v, sep='\n')
#    else: print(v)
   
# 140 다음 코드를 for문으로 작성하라.
# print("-------")
# print("-------")
# print("-------")
# print("-------")

# for i in range(4): print("-------")

# 141 다음과 같이 판매가가 저장된 리스트가 있을 때 부가세가 포함된 
# 가격을 for 문을 사용해서 화면에 출력하라. 단 부가세는 10원으로 가정한다.
# 리스트 = [100, 200, 300]
# for i in 리스트: print(i+10)

# 142 for 문을 사용해서 리스트에 저장된 값을 다음과 같이 출력하라.
# 리스트 = ["김밥", "라면", "튀김"]
# for i in 리스트: print(f"오늘의 메뉴 : {i}")

# 143 리스트에 주식 종목이름이 저장돼 있다.
# 리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
# for i in 리스트: print(len(i))

# 144 리스트에는 동물이름이 문자열로 저장돼 있다.
# 리스트 = ['dog', 'cat', 'parrot']
# for i in 리스트: print(i, len(i))

# 145 리스트에 동물 이름 저장돼 있다.
# 리스트 = ['dog', 'cat', 'parrot']
# for i in 리스트: print(i[0])

# 146 리스트에는 세 개의 숫자가 바인딩돼 있다.
# 리스트 = [1, 2, 3]
# for i in 리스트: print(f"3 x {i}")

# 147 리스트에는 세 개의 숫자가 바인딩돼 있다.
# 리스트 = [1, 2, 3]
# for i in 리스트: print(f"3 x {i} = {3*i}")

# 148 리스트에는 네 개의 문자열이 바인딩돼 있다.
# 리스트 = ["가", "나", "다", "라"]
# for i in 리스트[1:]: print(i)

# 149 리스트에는 네 개의 문자열이 바인딩돼 있다.
# 리스트 = ["가", "나", "다", "라"]
# 리스트 슬라이싱 [시작:끝:증감폭] 증감폭을 2로 설정해서 가, 다를 슬라이싱함
# for i in 리스트[::2]: print(i)

# 150 라, 다, 나, 가
# 리스트 = ["가", "나", "다", "라"]
# for i in 리스트[::-1]: print(i)

# 151 음수를 출력
# 리스트 = [3, -20, -3, 44]
# for i in 리스트:
#    if i < 0: print(i)

# 152 for문을 사용해서 3의 배수만을 출력하라.
# 리스트 = [3, 100, 23, 44]
# for i in 리스트:
#    if i % 3 == 0: print(i)

# 153 리스트에서 20 보다 작은 3의 배수를 출력하라
# 리스트 = [13, 21, 12, 14, 30, 18]
# for i in 리스트:
#    # 가독성을 위해 괄호로 구분
#    if (20 > i) and (i % 3 == 0): print(i)

# 154 리스트에서 세 글자 이상의 문자를 화면에 출력하라
# 리스트 = ["I", "study", "python", "language", "!"]
# for i in 리스트:
#    if len(i) >= 3: print(i)

# 155 리스트에서 대문자만 화면에 출력하라.
# 리스트 = ["A", "b", "c", "D"]
# for i in 리스트:
#    if i.isupper(): print(i)

# 156 리스트에서 소문자만 화면에 출력하라.
# 리스트 = ["A", "b", "c", "D"]
# for i in 리스트:
#    if not i.isupper(): print(i)

# 157 이름의 첫 글자를 대문자로 변경해서 출력하라.
# 리스트 = ['dog', 'cat', 'parrot']
'''
1) 인덱싱으로 첫번째 문자를 가져온다.
2) upper() 함수로 대문자로 변경한다.
3) 변경한 대문자와 나머지 문자를 이어붙인다.
'''
# for i in 리스트:
#    print(i[0].upper()+i[1:])

# 158 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 
# 화면에 출력하라. (힌트: split() 메서드)
# 리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
# for i in 리스트:
#    print(i.split('.')[0])

# 159 파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력하라.
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for i in 리스트:
#    if i.split('.')[1] == 'h' or i.split('.')[1] == 'c':
#       print(i)

# 161 for문과 range 구문을 사용해서 0~99까지 
# 한 라인에 하나씩 순차적으로 출력하는 프로그램을 작성하라.
# for i in range(100):
#    print(i)

# 162 월드컵은 4년에 한 번 개최된다. range()를 사용하여 
# 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하라.
# range의 세번 째 파라미터는 증감폭을 결정합니다.
# for i in range(2002, 2051, 4):
#    print(i)

# 163 1부터 30까지의 숫자 중 3의 배수를 출력하라.
# for i in range(3, 31, 3): print(i)

# 164 99부터 0까지 1씩 감소하는 숫자들을, 한 라인에 하나씩 출력하라.
# for i in range(99, -1, -1): print(i)

# 다른 방법
# for i in range(100):
#     print(99 - i)

# 165 for문을 사용해서 아래와 같이 출력하라.
# 0.0, 0.1 ~ 0.9
# for i in range(10): print(f"0.{i}")

# 다른방법
# for num in range(10) :
#     print(num / 10)

# 166 구구단 3단을 출력하라.
# for i in range(1, 10): print(f"3x{i} = {3*i}")

# 167 구구단 3단을 출력하라. 단 홀수 번째만 출력한다.
# for i in range(1, 10, 2):
#    print(f"3x{i} = {3*i}")

# 168 1~10까지의 숫자에 대해 모두 더한 값을 출력하는 프로그램을 
# for 문을 사용하여 작성하라.
# sum = 0
# for i in range(1, 11):
#    sum += i
# print(f"합 : {sum}")

# 169 1~10까지의 숫자 중 모든 홀수의 합을 출력하는 프로그램을 
# for 문을 사용하여 작성하라.
# sum = 0
# for i in range(1, 11, 2):
#    sum += i
# print(sum)

# 170 1~10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 
# for 문을 사용하여 작성하라.
# sum = 1
# for i in range(1, 11):
#    sum*=i
# print(sum)

# 171 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)): print(price_list[i])

# iterable : member를 하나씩 차례로 반환 가능한 object
# 예로는 sequence type인 list, str, tuple 

# iterator : next() 메서드로 데이터를 순차적으로 호출 가능한 object
# iterable을 iterator 로 변환하고 싶다면, iter() 사용
# x = [1,2,3] # Iterable 
# y = iter(x) # iterator
# print(f"x = {type(x)}\ny = {type(y)}")
# print(next(y)) 
# print(next(y))
# print(next(y))

# 172 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
# price_list = [32100, 32150, 32000, 32500]
# for i, v in enumerate(price_list): print(i, v)

# 173 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#    print((len(price_list)-1) - i, price_list[i])

# 174 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
# price_list = [32100, 32150, 32000, 32500]
# for i, v in enumerate(price_list[1:]):
#    print(str(i+10)+'0', price_list[i+1])

# for i in range(1, 4):
#    print(90+10*i, price_list[i])

# 175 my_list를 아래와 같이 출력하라.
'''
가 나
나 다
다 라
'''
# index간에 규칙관계를 파악해야함
# 첫번쨰 열에 index를 파악한후 
# 같은 행의 두 데이터는 인덱스 차이가 +1라는 것을 파악 
my_list = ["가", "나", "다", "라", ]
for i in range(len(my_list)-1):
   print(my_list[i], my_list[i+1])

print("-----")

for i in range(1, len(my_list)):
   print(my_list[i-1], my_list[i])


