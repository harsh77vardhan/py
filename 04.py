#05 factorial
fac=1
def factorial(n):
    global fac
    if n>=0:
        if n==0 or n==1:
         return fac
        else:
           factorial(n-1)
           fac=fac*n
           return fac

    else:
       print("invalide")

num=int(input("enter"))

print(factorial(num))

 





