n = int(input("введите число" ))
p1 = 0
p2 = 1
print(p1,p2, end=" ")
for i in range(1,n+1):
    print(p1+p2, end=" ")
    d=p1
    p1=p2
    p2= p1+d
print()
    
    
    
    