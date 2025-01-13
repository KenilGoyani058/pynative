#Check Palindrome Number
num=input("Enter Number : ")
n=len(num)
x=int(n/2)
status=0
for i in range(0,x):
    if num[i]==num[-1-i]:
        status=1
        #continue
    else:
        status=0

if status==1:
    print("Number is Palindrome")
else:
    print("Number is not Palindorme")