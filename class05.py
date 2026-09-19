# Check Neon number


n=int(input("Enter the number: "))

s=n*n


def sum_of_s(s):


    dig=s%10
    
    
    if s//10==0:
        return dig
    else:

        return dig+sum_of_s(s=s//10)


sm=sum_of_s(s)

if sm==n:
    print("is neo")

else:
    print(" isnt neo")