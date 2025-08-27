def swap(a,b):
    b=a+b
    a=b-a
    b=b-a
    print("After Swapping")
    print("a=",a,sep="")
    print("b=",b,sep="")
x=int(input("enter a value:"))
y=int(input("enter b value:"))
swap(x,y)