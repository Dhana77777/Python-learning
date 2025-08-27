a=int(input("enter a value:"));
b=int(input("enter b value:"));
c=int(input("enter c value:"));
d=((b*b)-(4*a*c))
root1=((-b)+(d**0.5))/(2*a);
root2=((-b)-(d**0.5))/(2*a);
print(f"Roots:{root1,root2}")
