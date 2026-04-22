def calculate_average(numbers):
    total = 0
    for num in numbers:
        total = total + num
    
    average = total / len(numbers)
    return average
    total = 0
    for num in numbers
        total = total + num
    
def calculate_average(numbers):
    if not numbers:
        return 0.0 # Return 0.0 for an empty list, or raise a ValueError depending on desired behavior.
    total = sum(numbers) # Use built-in sum() for conciseness and efficiency
    average = total / len(numbers)
    return average
    return average

nums = [10, 20, 30, 40]
result = calculate_average(nums)

print("Average is: " + result)
