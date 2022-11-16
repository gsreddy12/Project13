pattern=int(input('Enter Any Number of Rows:'))
for i in range(1,pattern+1):
    for j in range(1,i+1):
        print("*",end='\t')
    print()
print("--------1")
pattern=int(input('Enter Any Number of Rows:'))
for i in range(1,pattern+1):
    for j in range(i,pattern+1):
        print("*",end='\t')
    print()