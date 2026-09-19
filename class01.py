a = int(input("Enter the starting number: "))
b = int(input("Enter the ending number: "))

for i in range(a, b + 1):
    if i > 1:
        prime = True

        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                prime = False
                break

        if prime:
            print(i, end=" ")


    






