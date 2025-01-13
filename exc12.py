#Calculate income tax 0-10000 tax=0 next 10000 = 10% and next = 20%
income=int(input("Enter Your income: "))
tax=0

if income<=10000:
    print("Tax on income is ", tax)
elif income>10000:
    income-=10000
    if income<=10000:
        tax=tax+(income*0.1)
    elif income>10000:
        tax=tax+1000
        income=income-10000
        tax=tax+(income*0.2)

    print("Tax on income is : ",tax)