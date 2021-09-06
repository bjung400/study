# 2920
music = input().split()
    
ascending = [i for i in range(1, 9)]

music = list(map(int, music))

if music == ascending: print("ascending")
elif music == ascending[::-1]: print("descending")
else: print("mixed")


    
        
    
