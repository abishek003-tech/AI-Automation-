# T2-Function Challenge

# Create : find_second_largest(numbers)
# Example :
# Input:
# [10, 45, 23, 89, 45, 12]

# Output:
# 45
# Do not use sort()

def find_second_largest(numbers):
    largest = float('-inf')
    second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num

        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest


numbers = [10, 45, 23, 89, 45, 12]

result = find_second_largest(numbers)

print(result)