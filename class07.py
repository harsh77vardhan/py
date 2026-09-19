# Find quadratic roots of an equation

a=int(input("enter the coefficient of x^2: "))
b=int(input("enter the coefficient of x: "))
c=int(input("enter the constant term: "))

d=(b**2)-4*a*c
if d>=0:
    x=((-b)+(d**0.5))/(2*a)
    y=((-b)-(d**0.5))/(2*a)

    print(f"the roots are {x:.2f} and {y:.2f}")

else:
    print("roots are imaginary")

