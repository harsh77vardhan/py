# A grocery shop offers a 10% discount if the total purchase amount is over $100.
# Calculate the final payable amount.

n=int(input("Enter the amount in dollars:"))


if n>=100:
    print(f"you got the discount of 10% and your total is {n-(0.1*n)} ")

else:
    print(f"you got no discount and your total bill is of {n}")

