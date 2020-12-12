x= int(input(" введите количество денег"))
y= int(input(" введите процент"))
n= int(input("введите количество лет"))
for i in range(1,n+1,1):
    x=x+(y*x)/100
print(x)

    
    