hex_value=input("Enter the value: ")
binary=""
for x in hex_value:
    binary+=bin(int(x,16))[2:].zfill(4)

print(binary)