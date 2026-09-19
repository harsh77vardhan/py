'''Validate if a user can withdraw a requested cash amount based on available balance
and daily limit constraints.'''

balance=5000
withdrawl_history=0
while True:
    print("\      MENU      " )
    print("1.check balance" )
    print("2.withdraw" )
    print("3.exit" )
    n=int(input("Enter: "))

    if n==1:
        print(f"The current balance of youres is {balance}")

    elif n==2:
        m=int(input("Enter the amount you want to withdraw: "))
        if withdrawl_history<=5:
            if m<=balance:
                print(f"you have succesfully withdrawal {m}amount ")
                balance-=m
                withdrawl_history+=1
            else:
                print("insufficien fund")
        else:
            print("withdrawal limit exided")

    elif n==3:
        print("thanks")
        break
    else:
        print("invalide input")

    

        
    
    
    
    

   
   
