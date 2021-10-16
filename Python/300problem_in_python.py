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

# 098 098 딕셔너리 update 메서드
# 아래의 new_product 딕셔너리를 다음 icecream 딕셔너리에 추가하라.
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream = icecream + new_product
print(icecream)