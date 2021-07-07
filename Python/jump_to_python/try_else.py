try:
    age = int(input('나이을 입력하세요: '))
except:
    print("입력이 정확하지 않습니다.")
else:
    if age <= 18:
        print("미성년자 출입금지")
    else:
        print("환영합니다")