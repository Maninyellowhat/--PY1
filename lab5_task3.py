

from random import shuffle

def get_unique_list_numbers() -> list[int]:
    unic_list = [i for i in range(-10, 11)]
    shuffle(unic_list)
    unic_list = unic_list[:15]
    return unic_list

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
