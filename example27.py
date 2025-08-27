def quadratic(a,b,c):
    d=((b*b)-(4*a*c))
    root1=((-b)+(d**0.5))/(2*a);
    root2=((-b)-(d**0.5))/(2*a);
    print(f"Roots:{root1,root2}")
x=int(input("enter a value:"));
y=int(input("enter b value:"));
z=int(input("enter c value:"));
quadratic(x,y,z)