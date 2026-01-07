#Day 8 Multiplication Table
print(" Welcome to the Multiplication Table Generator ".center(60, "="))
num = int(input("Enter the desired number that you want to generate: "))
limit = int(input("Enter the limit up to which you want the table: "))
for i in range(1, limit + 1):
    print(f"{num} x {i} = {num * i}")