pattern=int(input('Enter Any Number of Rows:'))
for i in range(1,pattern+1):
    for j in range(i,pattern):
        print(" ",end=' ')
    for k in range(1,i+1):
        print('*  ',end=' ')
    for s in range(1,pattern+1):
        print(' ',end=' ')
    print("\n")

pattern=int(input('Enter Any Number of Rows:'))
for i in range(1,pattern+1):
    for j in range(1,pattern+i):
        print(" ",end=' ')
    for k in range(i,pattern+1):
        print('*  ',end=' ')
    for s in range(i,pattern-1):
        print(' ',end=' ')
    print("\n")
