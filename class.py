# # Python program to print all Prime numbers in an Interval


a= int(input("Enter the first no: "))
b= int(input("Enter the second no: "))

for i in range (a,b):

    prime=True


    



    for num in range(2,int(b**0.5)+1):
        if i%num==0:
            pass
        else:
            prime=False

    if prime and i>1:
        pass
    else:
        print(i)

    

      