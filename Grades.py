num1,num2,num3,num4,num5=map(int,input().split())
p=(num1+num2+num3+num4+num5)/5
if(p>=90):
    print("Grade A")
elif(p>=80):
    print("Grade B")
elif(p>=70):
    print("Grade C")
elif(p>=60):
    print("Grade D")
elif(p>=40):
    print("Grade E")
else:
    print("Grade F")