a= int(input(" введите число"))
b= int(input(" введите число"))
c= int(input("введите число"))
if (a+b)>c and (b+c)>a and (c+a)>b:
    print('существует')
    if a==b or a==c:
        print('равносторонний')
    elif a==b and a==c and b==c:
        print('равнобедренный')
    else:
        print('разносторонний')
else:
    print(0)
    
    
    