#problem to find greatest number of three numbers
def greatestnumberof3(a,b,c):
    if(a>=b and a>=c):
        print (a)
    elif (c>=a and c>=b):
        print (c)
    else:
        print (b)
    
#problem to find greatest number of three numbers
greatestnumberof3(3,99,9)

#-------------------------------
#Problem to convert ferenheit to celsius
def ferherniteTocelcius(fh):
    c= (fh - 32) * 5/9
    return c

f=float(input("Enter the temparature in ferenheit: "))
print((f"{ferherniteTocelcius(f):.2f}"))