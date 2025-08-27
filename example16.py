n=int(input("how many subjects u want to calculate the marks:"))
marks=0
for i in range(1,n+1):
    sub=int(input(f"enter the marks of {i}st subject:"))
    marks = marks + sub
avg = marks/n;
print(marks)
print(avg)
if(avg >= 90 and avg <=100):
    print("A grade")
elif (avg >= 80 and avg < 90):
    print("B grade")
elif (avg >= 70 and avg <80):
    print("C grade")
elif(avg >= 60 and avg <70):
    print("D grade")
elif(avg >= 50 and avg <60):
    print("E garde")
else:
    print("fail")
