a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

add = a + b
sub = a - b
mul = a * b

if b != 0:
    div = a/b
else:
    div = "Undefined (Cannot divide by zero)"

print("\n")

print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)
