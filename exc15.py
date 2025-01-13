#Get an int value of base raises to the power of exponent
n=int(input("Enter Base : "))
x=int(input("Enter Exponent: "))
def exponent(base,exp):
    result=base**exp
    print(base," raise to the power of ",exp," is ",result)
exponent(n,x)