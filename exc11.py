#Get each digit from a number in the reverse order.
num=input("Enter number : ")
n=len(num)
str=""
for i in range(0,n):
    print(num[-1-i],end=" ")
