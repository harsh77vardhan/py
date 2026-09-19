hex_value = input("Enter hexadecimal value: ")

binary = ""

for digit in hex_value:
    if digit == "0":
        binary += "0000"
    elif digit == "1":
        binary += "0001"
    elif digit == "2":
        binary += "0010"
    elif digit == "3":
        binary += "0011"
    elif digit == "4":
        binary += "0100"
    elif digit == "5":
        binary += "0101"
    elif digit == "6":
        binary += "0110"
    elif digit == "7":
        binary += "0111"
    elif digit == "8":
        binary += "1000"
    elif digit == "9":
        binary += "1001"
    elif digit.upper() == "A":
        binary += "1010"
    elif digit.upper() == "B":
        binary += "1011"
    elif digit.upper() == "C":
        binary += "1100"
    elif digit.upper() == "D":
        binary += "1101"
    elif digit.upper() == "E":
        binary += "1110"
    elif digit.upper() == "F":
        binary += "1111"

print("Binary:", binary)