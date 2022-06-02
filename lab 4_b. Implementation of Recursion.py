def product(x, y):
    if x < y:
        return product(y, x)
    elif y != 0:
        return (x + product(x, y - 1))
    else:
        return 0

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print("The product of", x, "and", y, "is", product(x, y))





