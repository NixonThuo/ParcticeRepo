def sum_large(numbers):
    if len(numbers) > 1:
        numbers.sort()
        new_list = []
        new_list.append(numbers[0] + numbers[-1])
        numbers.pop(0)
        numbers.pop(-1)
        return new_list.append(sum_large(numbers))
    else:
        return new_list


print sum_large([1, 2, 5, 9, 7, 6])

"""
numbers = [1, 2, 5, 9, 7, 6]
numbers.pop(-1)
print numbers
"""
