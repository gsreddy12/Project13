pattern=int(input('Enter Any Number of Rows:'))
for i in range(1,pattern+1):
    for j in range(1,i+1):
        print(j,end='\t')
    print()
pattern=int(input('Enter Any Number of Rows:'))
for i in range(1,pattern+1):
    for j in range(i,pattern+1):
        print(j,end='\t')
    print()