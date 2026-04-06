n = int(input("Enter a number: "))
Rename the variable `sum` to a more descriptive name that does not conflict with built-in functions, such as `total_sum` or `even_sum`.

for i in range(1, n + 1):
    if i % 2 == 0:
You can simplify the code by directly adding `i` to `sum`: `sum = sum + i`.
        sum = sum + temp

print("Sum is:", sum)
