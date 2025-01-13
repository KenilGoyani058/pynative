#Remove first n characters from a string
def remove_char(str,n):
    str1=str[n:]
    print(str1)

str=input("Enter String : ")
n=int(input("Enter Character to Remove : "))
remove_char(str,n)