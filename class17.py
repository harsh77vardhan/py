# Calculate an employee's total weekly pay, paying 1.5x regular rate for hours worked
# beyond 40 hours
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

if hours <= 40:
    pay = hours * rate
else:
    pay = (40 * rate) + ((hours - 40) * rate * 1.5)

print("Total weekly pay =", pay)
