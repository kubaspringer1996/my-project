numbers= []
numbers_str = []
n = int(input("Enter n:"))
for i in range (n):
    i = int(input("Enter a number:"))
    numbers.append(i)
    numbers_str.append(str(i))

a = sum(numbers)
b = a//n
x = " ".join(numbers_str)

print(f"Enter a number: {x}")
print(f"Sum: {a}")
print(f"average: {b}")
if a > b:
    print("The sum is greater!")
