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
# my_list = ["가", "나", "다", "라", ]
# for i in range(len(my_list)-1):
#    print(my_list[i], my_list[i+1])

# print("-----")

# for i in range(1, len(my_list)):
#    print(my_list[i-1], my_list[i])

# 176 리스트를 아래와 같이 출력하라.
# my_list = ["가", "나", "다", "라", "마"]
# for i in range(len(my_list)-2):
#   print(my_list[i], my_list[i+1], my_list[i+2])

# 177 반복문과 range 함수를 사용해서 my_list를 아래와 같이 출력하라.
# my_list = ["가", "나", "다", "라"]
# for i in range(len(my_list)-1, 0, -1):
#   print(my_list[i], my_list[i-1])

# 178 리스트에는 네 개의 정수가 저장되어 있다. 각각의 데이터에 대해서 자신과 우측값과의 차분값을 화면에 출력하라.
# my_list = [100, 200, 400, 800]
# for i in range(len(my_list)-1):
#   print(abs(my_list[i+1]-(my_list[i])))

# 179 리스트에는 6일 간의 종가 데이터가 저장되어 있다. 종가 데이터의 3일 이동 평균을 계산하고 이를 화면에 출력하라.
# my_list = [100, 200, 400, 800, 1000, 1300]
# for i in range(len(my_list)-2):
#   print(abs(my_list[i]+my_list[i+1]+my_list[i+2])/3)

# 180 리스트에 5일간의 저가, 고가 정보가 저장돼 있다. 고가와 저가의 차를 변동폭이라고 정의할 때, low, high 두 개의 리스트를 사용해서 5일간의 변동폭을 volatility 리스트에 저장하라.
# low_prices  = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]
# volatility = []
# for i in range(len(low_prices)):
#   volatility.append(high_prices[i]-low_prices[i])
# print(volatility)

# 181 아래 표에서 하나의 행을 하나의 리스트로, 총 3개의 리스트를 갖는 이차원 리스트 apart를 정의하라.
# apart = [["101호", "102호"], ["201호", "202호"],["301호", "302호"]]

# 182 아래 표에서 하나의 열을 하나의 리스트로, 총 2개의 리스트를 갖는 이차원 리스트 stock을 정의하라.
# stock = [["시가", 100, 200, 300], ["종가", 80, 210, 330]]
# for i in stock:
#   for j in i:
#     print(j)
#   print("-----")

# 183 아래 표를 stock 이름의 딕셔너리로 표현하라.key로 저장하고, 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다.
# stock = {"market_price":[100, 200, 300],"closing_price":[80, 210, 330]}
# print(stock)

# 184 아래 표를 stock 이라는 이름의 딕셔너리로 표현하라. 날짜를 key로 저장하고, 나머지 같은 행의 데이터를 리스트로 저장해서 value로 저장한다. 첫 열이 날짜이다.
# stock = {"10/10":[80, 110, 70, 90],"10/11":[210,230,190,200]}
# print(stock)

# 185 리스트에 저장된 데이터를 아래와 같이 출력하라.
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for row in apart:
#   for col in row:
#     print(f"{col}호")

# 186 리스트에 저장된 데이터를 아래와 같이 출력하라.
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for low in apart[::-1]:
#   for col in low:
#     print(f"{col}호")

# 187 리스트에 저장된 데이터를 아래와 같이 출력하라.
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in apart[::-1]:
#   for j in i[::-1]:
#     print(f"{j}호")

# 188 리스트에 저장된 데이터를 아래와 같이 출력하라.
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for row in apart:
#   for col in row:
#     print(f"{col}호")
#     print('-'*5)

# 189 리스트에 저장된 데이터를 아래와 같이 출력하라.
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for row in apart:
#   for col in row:
#     print(f"{col}호")
#   print('-'*5)

# 190 리스트에 저장된 데이터를 아래와 같이 출력하라.
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for row in apart:
#   for col in row:
#     print(f"{col}호")
# print('-'*5)

# 191 data에는 매수한 종목들의 OHLC (open/high/low/close) 가격 정보가 바인딩 되어있다.
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# for row in data:
#   for col in row:
#     print(col*1.00014)

# 192 191번의 출력 결과에 행단위로 "----" 구분자를 추가하라.
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# for row in data:
#   for col in row:
#     print(col*1.00014)
#   print('-'*4)

# 193 192 번 문제의 결괏값을 result 이름의 리스트에 1차원 배열로 저장하라.
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# result = []
# for row in data:
#   for col in row:
#     result.append((col*1.00014))
# print(result)

# 194 191번 문제의 결괏값을 result 이름의 리스트에 2차원 배열로 저장하라. 저장 포맷은 아래와 같다. 각 행에 대한 데이터끼리 리스트에 저장되어야 한다.
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# result = []
# for row in data:
#   sub = []
#   for col in row:
#     sub.append((col*1.00014))
#   result.append(sub)
# print(result)

# 195 ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 화면에 종가데이터를 출력하라.
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for row in ohlc[1:]:
#   print(row[3])

# 196 ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 종가가 150원보다 큰경우에만 종가를 출력하라.
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for row in ohlc[1:]:
#   if row[3] > 150: print(row[3])

# 197 ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 종가가 시가 보다 크거나 같은 경우에만 종가를 출력하라.
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for row in ohlc[1:]:
#   if row[0] <= row[3]:
#     print(row[3])

# 198 ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 고가와 저가의 차이를 변동폭으로 정의할 때 변동폭을 volatility 이름의 리스트에 저장하라.
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# volatility = []
# for row in ohlc[1:]:
#   volatility.append(row[1]-row[2])
# print(volatility)

# 199 리스트에는 3일 간의 ohlc 데이터가 저장돼 있다. 종가가 시가보다 높은 날의 변동성 (고가 - 저가)을 화면에 출력하라.
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for row in ohlc[1:]:
#   if row[3] > row[0]: print(row[1]-row[2])

# 200 리스트에는 3일 간의 ohlc 데이터가 저장돼 있다. 시가에 매수해서 종가에 매도 했을 경우 총 수익금을 계산하라.
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# profit = 0
# for row in ohlc[1:]:
#   profit += row[3]-row[0]
# print(profit)

# 09. 파이썬 함수 함수란 자주 사용하는 코드에 대한 이름표입니다. 
# 변수가 어떤 값을 바인딩하는 것처럼 함수는 어떤 코드를 바인딩합니다.

# 201 "비트코인" 문자열을 화면에 출력하는 print_coin() 함수를 정의하라.
# def print_coin():
#   print("비트코인")

# 202 201번에서 정의한 함수를 호출하라.
# print_coin()

# 203 201번에서 정의한 print_coin 함수를 100번호출하라.
# for i in range(100):
#   print_coin()

# 204 "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라.
# def print_coin():
#   for i in range(100):
#     print("비트코인")
# print_coin()

# 205 아래의 에러가 발생하는 이유에 대해 설명하라.
# 함수 정의 전에 호출했기때문이다.
# hello()
# def hello():
#     print("Hi")

# 206 아래 코드의 실행 결과를 예측하라.
# A B C A B
# def message() :
#     print("A")
#     print("B")

# message()
# print("C")
# message()

# 207 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)
# A C B
# print("A")

# def message() :
#     print("B")

# print("C")
# message()

# 208 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)
# A C B E D
# print("A")
# def message1() :
#     print("B")
# print("C")
# def message2() :
#     print("D")
# message1()
# print("E")
# message2()

# 209 아래 코드의 실행 결과를 예측하라.
# B A
# def message1():
#     print("A")

# def message2():
#     print("B")
#     message1()

# message2()

# 210 아래 코드의 실행 결과를 예측하라.
# B C B C B C A
# def message1():
#     print("A")

# def message2():
#     print("B")

# def message3():
#     for i in range (3) :
#         message2()
#         print("C")
#     message1()

# message3()

# 211 함수의 호출 결과를 예측하라.
# 안녕 Hi
# def 함수(문자열) :
#     print(문자열)

# 함수("안녕")
# 함수("Hi")

# 212 함수의 호출 결과를 예측하라.
# 7 15
# def 함수(a, b) :
#     print(a + b)

# 함수(3, 4)
# 함수(7, 8)

# 213 아래와 같은 에러가 발생하는 원인을 설명하라.
# 함수의 정의와 다르게 호출하고있다.
# 함수를 호출할때 하나의 파라미터를 입력해야한다.
# def 함수(문자열) :
#     print(문자열)
# 함수()

# 214 아래와 같은 에러가 발생하는 원인을 설명하라.
# 두개의 값을 입력받아 덧셈연산을 하려는 의도로 설계된 함수인데
# 호출할때 문자열과 숫자를 입력해서 서로 더할수 없다는 에러가 발생합니다.
# def 함수(a, b) :
#     print(a + b)

# 함수("안녕", 3)

# 215 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.
# def print_with_smile(s):
#   print(s+":D")

# 216 215에서 정의한 함수를 호출하라. 파라미터는 "안녕하세요"로 입력하라.
# print_with_smile("안녕하세요")

# 217 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.
# def print_upper_price(price):
#   print(price*1.3)

# 218 두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라.
# def print_sum(a, b):
#   print(a+b)

# 219 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.
# def print_arithmetic_operation(a, b):
#   print(f"{a} + {b} = {a+b}")
#   print(f"{a} - {b} = {a-b}")
#   print(f"{a} * {b} = {a*b}")
#   print(f"{a} / {b} = {a/b}")

# print_arithmetic_operation(3, 4)

# 220 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.
# def print_max(a, b, c):
#   max_val = 0
#   if a > max_val:
#     max_val = a
#   if b > max_val:
#     max_val = b
#   if c > max_val:
#     max_val = c
#   print(max_val)

# print_max(1,2,3)

# 221 입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의하라.
# def print_reverse(string):
#   print(string[::-1])
# print_reverse("python")
    
# 222 성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 정의하라.
# def print_score(score_list):
#   print(sum(score_list)/len(score_list))
# print_score([1,2,3])

# 223 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.
# def print_even(l):
#   for i in l:
#     if i % 2 == 0: print(i)
# print_even ([1, 3, 2, 10, 12, 11, 15])

# 224 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.
# def print_keys(dic):
#   for i in dic.keys(): print(i)
# print_keys({"이름":"김말똥", "나이":30, "성별":0})

# 225 my_dict에는 날짜를 키값으로 OHLC가 리스트로 저장돼 있다.
# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}
# my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의하라.
# def print_value_by_key(dict, key):
#   print(dict[key])
  
# print_value_by_key(my_dict, "10/26")

# 226 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.
# def print_5xn(str):
#   length = 5
#   print([str[i:i+length]for i in range(0, len(str), length)])

# def print_5xn(str):
#   for i in range(0, len(str), 5):
#     print(str[i:i+5])

# def print_5xn(line):
#   chunk_num = int(len(line) / 5)
#   for i in range(chunk_num):
#     print(line[i*5:i*5+5])
# print_5xn("아이엠어보이유알어걸")

# 227 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.
# def print_mxn(str,length):
#   chunk_num = int(len(str)/length)
#   for i in range(chunk_num+1):
#     print(str[i*length:i*length+length])
# print_mxn("아이엠어보이유알어걸", 3)

# 228 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라. 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.
# def calc_monthly_salary(annual_salary):
#   monthly_pay = int(annual_salary / 12)
#   return monthly_pay

# print(calc_monthly_salary(12000000))

# 229 아래 코드의 실행 결과를 예측하라.
# 왼쪽: 100, 오른쪽: 200
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)

# my_print(a=100, b=200)

# 230 아래 코드의 실행 결과를 예측하라.
# 왼쪽: 200, 오른쪽: 100
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)

# my_print(b=100, a=200)

# 231 아래 코드를 실행한 결과를 예상하라.
# name result is not defined
# def n_plus_1 (n) :
#     result = n + 1

# n_plus_1(3)
# print (result)

# 232 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
# def make_url(address):
#   return(f"www.{address}.com")
# print(make_url("naver"))

# 233 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.
# def make_list(str):
#   return [i for i in str]
# def make_list(str):
#   return list(str)
# print(make_list("abcd"))

# 234 숫자로 구성된 하나의 리스트를 입력받아, 
# 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.
# def pickup_even(l):
#   return [i for i in l if i % 2 == 0]
# print(pickup_even([3, 4, 5, 6, 7, 8]))

# 235 콤마가 포함된 문자열 숫자를 입력받아 정수로 
# 변환하는 convert_int 함수를 정의하라.
# def convert_int(str):
#   return int(str.replace(',', ''))
# print(convert_int("1,234,567"))

# 236 아래 코드의 실행 결과를 예측하라.
# 22
# def 함수(num) :
#     return num + 4

# a = 함수(10)
# b = 함수(a)
# c = 함수(b)
# print(c)

# 237 아래 코드의 실행 결과를 예측하라.
# 22
# def 함수(num) :
#     return num + 4

# c = 함수(함수(함수(10)))
# print(c)

# 238 아래 코드의 실행 결과를 예측하라.
# 140
# def 함수1(num) :
#     return num + 4

# def 함수2(num) :
#     return num * 10

# a = 함수1(10)
# c = 함수2(a)
# print(c)

# 239 아래 코드의 실행 결과를 예측하라.
# 16
# def 함수1(num) :
#     return num + 4

# def 함수2(num) :
#     num = num + 2
#     return 함수1(num)

# c = 함수2(10)
# print(c)

# 240 아래 코드의 실행 결과를 예측하라.
# 28
# def 함수0(num) :
#     return num * 2

# def 함수1(num) :
#     return 함수0(num + 2)

# def 함수2(num) :
#     num = num + 10
#     return 함수1(num)

# c = 함수2(2)
# print(c)

# 10. 파이썬 모듈 파이썬 모듈은 파이썬 파일을 의미합니다. 파이썬은 다양한 분야별로 모듈을 제공합니다. 프로그램 구현에 필요한 모듈의 기초 사용법을 알아봅시다.

# 241 현재시간 datetime 모듈을 사용해서 현재 시간을 화면에 출력해보세요.
# import datetime
# print(datetime.datetime.now())

# 242 현재시간의 타입 datetime 모듈의 now 함수의 리턴 값의 타입을 화면에 출력해보세요.
# import datetime
# now = datetime.datetime.now()
# print(now, type(now))

# 243 timedelta datetime 모듈의 timedelta를 사용해서 
# 오늘로부터 5일, 4일, 3일, 2일, 1일 전의 날짜를 화면에 출력해보세요.
# import datetime 
# today = datetime.date.today()
# for i in range(5, 0, -1):
#   delta = datetime.timedelta(days=i)
#   print(f"{i}일 전 날짜는 : {today - delta}")

# 244 strftime 현재시간을 얻어온 후 다음과 같은 포맷으로 시간을 출력해보세요. strftime 메서드를 사용하세요.
# import datetime

# now = datetime.datetime.now()
# print(now.strftime('%H:%M:%S'))

# 245 strptime datetime.datetime.strptime 메서드를 사용하면 문자열 형식의 시간을 datetime.datetime 타입의 시간 값으로 만들어줍니다. "2020-05-04"의 문자열을 시간 타입으로 변환해보세요.
# import datetime
# day = "2020-05-04 11:11:11"
# ret = datetime.datetime.strptime(day, '%Y-%m-%d %H:%M:%S')
# print(ret, type(ret))

# 246 sleep 함수 time 모듈, datetime 모듈을 사용해서 1초에 한 번 현재 시간을 출력하는 코드를 작성하세요.
# import time, datetime

# while True:
#   now = datetime.datetime.now()
#   print(now.strftime('%H:%M:%S'))
#   time.sleep(1)

# 247 모듈 임포트 모듈을 임포트하는 4가지 방식에 대해 설명해보세요.
# import os # A module import
# from os import listdir # from B import A
# from A import * # bring everything from A (이방법은 충돌이 발생할수있음)
# import backtrader as bt # bacltrader module을 bt라는 이름으로 사용하겠음

# 248 os 모듈 os 모듈의 getcwd 함수를 호출하여 현재 디렉터리의 경로를 화면에 출력해보세요.
# import os
# ret = os.getcwd()
# print(ret, type(ret))

# 249 rename 함수 바탕화면에 텍스트 파일을 하나 생성한 후 os 모듈의 rename 함수를 호출하여 해당 파일의 이름을 변경해보세요.
# import os
# os.rename('t', "test")

# 250 numpy 모듈의 arange 함수를 사용해서 0.0 부터 5.0까지 0.1씩 증가하는 값을 화면에 출력해보세요.
# import numpy
# for i in numpy.arange(0, 5, 0.1):
#   print(float(i))

# 11. 파이썬 클래스 파이썬 클래스는 타입을 만들어내는 도구입니다. 
# int, float, str과 같이 여러분의 새로운 타입을 만들 수 있습니다.

# 251 클래스, 객체, 인스턴스에 대해 설명해봅시다.
# Class : 똑같은 무엇인가를 계속 만들어 낼수있는 설계, 틀 (설계도)
# Method : 클래스 내부에 저의된 함수
# Object : 실제로 만들어진 자동차

# Instance : 클래스의 의해서 만들어진 객체 
# 어떤 클래스의 객체인지를 관계위주로 설명할때 사용

# 252 비어있는 사람 (Human) 클래스를 "정의" 해보세요.
# class Human():
#   pass

# 253 인스턴스 생성 사람 (Human) 클래스의 인스턴스를 "생성" 하고 이를 areum 변수로 바인딩해보세요.
# class Human():
#   pass

# areum = Human()

# 254 사람 (Human) 클래스에 "응애응애"를 출력하는 생성자를 추가하세요.
# class Human():
#   def __init__(self):
#     print("응애응애")

# areum = Human()

# 255 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요.
# class Human():
#   def __init__(self, name, age, sex):
#     self.name = name
#     self.age = age
#     self.sex = sex
    
# areum = Human("아름", 25, "여자")
# print(areum.name)

# 256 255에서 생성한 인스턴스의 이름, 나이, 성별을 출력하세요. 
# 인스턴스 변수에 접근하여 값을 출력하면 됩니다.
# class Human():
#   def __init__(self, name, age, sex):
#     self.name = name
#     self.age = age
#     self.sex = sex
    
# areum = Human("아름", 25, "여자")
# print(f"이름 : {areum.name}, 나이 : {areum.age}, 성별 : {areum.sex}")

# 257 사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.
# class Human():
#   def __init__(self, name, age, sex):
#     self.name = name
#     self.age = age
#     self.sex = sex

#   def who(self):
#     print(f"이름 : {self.name}, 나이 : {self.age}, 성별 : {self.sex}")

# areum = Human("종열", 26, "남자")
# areum.who()

# 258 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가하세요.
# class Human():
#   def __init__(self, name, age, sex):
#     self.name = name
#     self.age = age
#     self.sex = sex

#   def who(self):
#     print(f"이름 : {self.name}, 나이 : {self.age}, 성별 : {self.sex}")

#   def setInfo(self, name, age, sex):
#     self.name = name
#     self.age = age
#     self.sex = sex

# areum = Human("모름", 0, "모름")
# areum.who()

# areum.setInfo("아름", 25, "여자")
# areum.who()

# 259 사람 (human) 클래스에 "나의 죽음을 알리지 말라"를 출력하는 소멸자를 추가하세요.
# class Human():
#   def __init__(self, name, age, sex):
#     self.name = name
#     self.age = age
#     self.sex = sex

#   def __del__(self):
#     print("나의 죽음을 알리지 말라")
  
#   def who(self):
#     print(f"이름 : {self.name}, 나이 : {self.age}, 성별 : {self.sex}")

#   def setInfo(self, name, age, sex):
#     self.name = name
#     self.age = age
#     self.sex = sex


# areum = Human("아름", 25, "여자")
# del areum

# 260 아래와 같은 에러가 발생한 원인에 대해 설명하세요.
# # print() 함수는 0의 인수를 취하지만 1이 주어졌습니다.
# class OMG: 
#   def print(): # def print(self):
#     print("Oh my god")

# mystock = OMG()
# mystock.print()
# 클래스 객체를 생성할 때 만들어진 객체가
# 메서드를 호출 할 때 객체 자기 자신이 인자로 들어가기 때문입니다.
# 그래서 첫 번째 인자인 self가 들어가지 않으면 에러가 난다.

# 261 주식 종목에 대한 정보를 저장하는 Stock 클래스를 정의해보세요. 클래스는 속성과 메서드를 갖고 있지 않습니다.
# class Stock:
#   pass

# 262 Stock 클래스의 객체가 생성될 때 종목명과 종목코드를 입력 받을 수 있도록 생성자를 정의해보세요.
# class Stock:
#   def __init__(self, name, code):
#       self.name = name
#       self.code = code

# 삼성 = Stock("삼성전자", "005930")
# print(삼성.name)
# print(삼성.code)

# 263 객체에 종목명을 입력할 수 있는 set_name 메서드를 추가해보세요.
class Stock:
  def __init__(self, name, code):
    self.name = name
    self.code = code
  
  def set_name(self, name):
    self.name = name

삼성 = Stock("none", "005930")
print(삼성.name)

삼성.set_name("삼성전자")
print(삼성.name)






