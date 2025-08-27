s=input("enter the numbers")
a,b,c=s.split(",")
x=int(a)
y=int(b)
z=int(c)
if(x>y and x>z):
    print("The largest value is:",x,sep="")
elif(y>x and y>z):
    print("The largest value is:",y,sep="")
else:
    print("The largest value is:",z,sep="")