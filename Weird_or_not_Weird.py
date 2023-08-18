a=int(input())
if a%2!=0:
    print("weird")
elif a%2==0 and a>=2 and a<=5:
    print("not weird")
elif a%2==0 and a>=6 and a<=20:
    print("weird")
elif a%2==0 and a>20:
    print("not weird")
