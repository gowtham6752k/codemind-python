n=int(input())
x=n**2
y=(x-1)%9+1
if y==n:
    print("Neon Number")
else:
    print("Not Neon Number")