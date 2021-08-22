# q1 문자열 바꾸기
# str = "a:b:c:d"
# print('#'.join(str.split(':')))

# q2 딕셔너리 값 추출하기
# get 함수를 사용하면 해당 key가 없을 경우에는 두번째 매개변수로 전달된 default 값을 대신 돌려준다.
# a = {'A':90, 'B':80}
# print(a.get('C', 70))

# q3 리스트의 더하기와 extend 함수
# a = [1, 2, 3]
# a = a + [4, 5]
# print(a)

a = [1, 2, 3]
a = a + [4, 5]
# a.extend([4, 5]) # 리스트 끝에 iterable의 모든 항목을 넣습니다.
print(id(a))

