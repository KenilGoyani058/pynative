#Print the following pattern
n1=int(input("Enter number : "))
for i in range(1,n1+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print('\n')