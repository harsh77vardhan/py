'''Write a program to print the following number pattern up to n rows:
1
1 2
1 2 3
1 2 3 4'''


n=int(input("Enter the number: "))
i=1

for i in range(1,n+1):

    for n in range(1,i+1):
        print(n,end=" ")
    print()





    
