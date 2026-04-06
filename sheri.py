n = int(input("Enter a number: "))
sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
You can simplify the code by directly adding `i` to `sum`: `sum = sum + i`.
        sum = sum + temp

print("Sum is:", sum)
