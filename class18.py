pi = 3.14

wire = 400 * 100      # meters to centimeters
radius = 3

circumference = 2 * pi * radius

circles = wire // circumference

print("Number of circles =", int(circles))