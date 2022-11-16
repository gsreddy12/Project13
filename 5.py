pattern=int(input('Enter Any Number of Rows:'))
for i in range(pattern,0,-1):
    for j in range(i,0,-1):
        print(j,end='\t')
    print()
pattern=int(input('Enter Any Number of Rows:'))
p=pattern
for i in range(1,pattern+1):
    for j in range(p,i-1,-1):
        print(j,end='\t')
    print()