# Author: Aaron Amran
# Creation Date: 07th November 2022
# Quicksort algorithm with user-defined array values

import re
import numpy

print("\nThis program contains the quicksort algorithm. ")

# function to determine point of separation
def separate(user_array, low, high):
    # element at the most right is set as pivot
    pivot_element = user_array[high]

    # pointer for greater element
    i = low - 1

    # loop to go through all elements and compare with pivot
    for j in range(low, high):
        if user_array[j] <= pivot_element:
            # swap element smaller than pivot with the greater element pointed by i
            i = i + 1

            # swapping element at i with element at j
            (user_array[i], user_array[j]) = (user_array[j], user_array[i])

    # swap the pivot element with the greater element specified by i
    (user_array[i + 1], user_array[high]) = (user_array[high], user_array[i + 1])

    # return separation position
    return i + 1


def quicksort(user_array, low, high):
    if low < high:
        # elements smaller than pivot are on the left
        # elements larger than pivot are on the right
        pivot = separate(user_array, low, high)

        quicksort(user_array, low, pivot - 1)
        quicksort(user_array, pivot + 1, high)


# section for user prompt and input

array_input = []
num_format = re.compile("^-?[0-9]\d*(\.\d+)?$")


array_size = int(input("Please define the array size: "))

#  one cannot iterate over the list and modify it at the same time
for i in range(0, array_size):
    array_elements = input("\nPlease input number to fill in the array: ")
    is_number = re.match(num_format, array_elements)

    if is_number:
        array_input.append(array_elements)
    else:
        print('Please only use numerical digits.')


quicksort(array_input, 0, array_size - 1)
print('\nOutput of sorted array in ascending order: ')
print(array_input)
