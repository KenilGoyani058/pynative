#Print a downward half-pyramid pattern of stars
n1=int(input("Enter number : "))
for i in range(n1,0,-1):
    for j in range(i,0,-1):
        print('*',end=" ")
    print('\n')