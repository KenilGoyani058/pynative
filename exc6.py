#Display numbers divisible by 5
list1=input("Enter numbers by space : ").split()

list1 = [int(i) for i in list1]
print(list1)
for i in list1:
    if i % 5 == 0:
        print(i)
    else:
        continue