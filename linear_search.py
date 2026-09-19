a=[1,2,3,4,5,6,7,8,9,10]   
n= len(a)


def linearsearch(a,n,item):
    loc=-1
    i=0

    while i<n:
        if a[i]!=item:
            i+=1
            
        elif item==a[i]:
            print(i)
            return

        else:
            return loc


item=int(input("Enter the number: "))

linearsearch(a,n,item)


