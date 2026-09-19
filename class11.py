# Write a Python program to calculate a person's Body Mass Index (BMI) and classify it into
# one of the following categories using if-elif-else statements:
# BMI is calculated using the formula: BMI=weight (kg)/ height (m 2 )
# The program should take the person weight (in kg) and height (in m) as input, compute the
# BMI, and classify it as follows:
# BMI &lt; 18.5 Underweight
# 18.5 ≤ BMI &lt; 25 Normal
# 25 ≤ BMI &lt; 30 Overweight
# BMI ≥ 30 Obese

w=int(input("Enter your weight(in kgs) :"))
h=float(input("Enter your height(in  metres) :"))
bmi=w/(h**2)

if bmi>=18.5 and bmi<=25:
    print(f"your bmi is pretty normal,which is {bmi}")
elif bmi<18.5:
    print("you're underweight")
else:
    print("you're overweight ")


