#sum of squares of the numbers 

s=0
i=1

def sum_squares(i,n):
    global s


    
    if n>0 and i<=n and i>0:
        o=i*i
        s=s+o
        
        return sum_squares(i+1,n)
    elif n==0:
        return s
    else:
        return s
    


m=int(input("ENter the number: "))
print(sum_squares(i,m))