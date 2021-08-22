import sys

option = sys.argv[1]

# input
if option == '-a':
    memo = sys.argv[2:]
    f = open('memo.txt', 'a')
    f.write('S2'.join(memo))
    f.write('\n')
    f.close

# print
elif option == '-v':
    f = open('memo.txt', 'r')
    memo = f.read()
    f.close()
    print(memo)
elif option=="-c":
    f=open("memo.txt",'w')
    f.write("")
    f.close() 