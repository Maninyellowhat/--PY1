list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max_array = list_numbers[0]
max_array_ind = 0

num2 = list_numbers[-1]
for i in range(0, len(list_numbers)):
    if max_array < list_numbers[i]:
        max_array = list_numbers[i]
        max_array_ind = i
list_numbers[max_array_ind], list_numbers[-1] = list_numbers[-1], max_array
print(list_numbers)
