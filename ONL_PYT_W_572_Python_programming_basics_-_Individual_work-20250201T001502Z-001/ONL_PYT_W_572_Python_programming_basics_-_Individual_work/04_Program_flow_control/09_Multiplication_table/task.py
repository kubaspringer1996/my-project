n = int(input("Entered number:"))
if 0 < n <= 10:
    for i in range(1,11):
        x = i*n
        print(f"{i} * {n} = {x}")
