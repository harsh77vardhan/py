def train_ticket():
    n=int(input("enter the number of passengers: "))

    passanger_list=[]
    for i in range(n):

        pnr=input("enter the pnr number: ")
        name=input("enter the name of the passanger: ")
        age=int(input("enter the age:"))
        source=input("enter the source of the passanger: ").strip().lower()
        dest=input("enter the destinataion of the passanger: ").strip().lower()
        fare=float(input("enter the price of the ticket: "))

        passanger_tuple=(pnr,name,age,source,dest,fare)
        passanger_list.append(passanger_tuple)

    passanger=tuple(passanger_list)

    print("search passangers by source and destination")
    search_src=input("enter the souce of passanger: ").strip().lower()
    search_dest=input("enter the destination of passanger: ").strip().lower()

    matching_list=[p for p in passanger if p[3]==search_src and p[4]==search_dest]

    for p in matching_list:
        print(f" the pnr number is {p[0]}, passanger name is {p[1]}, age {p[2]} , fare  {p[5]}")


    
    max_fair=max(passanger, key=lambda p: p[5])
    max_n=(max_fair[1])
    print(f" the maximum fare is {max_n}")

    Sum=0
    for p in passanger:
        Sum+=p[5]

    print(f"the average fare for this n number if passangers is {Sum/n}")

    shorted_passangers=sorted(passanger, key=lambda p: p[5])

    for p in shorted_passangers:
        
        print(f"{p[5]}:{p[1]}")



train_ticket()

    

            














