str=input("enter the string:")
count=0
count1= len(str)
s=str.lower()
for i in range(count1):
    if(s[i]== 'a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
        count=count+1
print("Number of Vowels:",count,sep="")