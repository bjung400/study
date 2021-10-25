coffee = 5
while True:
    money = int (input("돈을 넣어주세요"))
    if money == 777:
        while True:
            print("잭팟 777")
    if money >= 300 and coffee > 0:
        money -= 300
        print("거스름돈 %d원과 커피를 줍니다." % (money))
        coffee -= 1
    elif money < 300:
        print("%d원을 돌려주고 커피안줍니다." % money)
        print("남은 커피의 양은 %d" % coffee)
    else:
        print("커피 다떨어져서 판매중지합니다.")

    


    
    
    
