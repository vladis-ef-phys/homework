import random

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        #a = random.randint(0, len(array)-1)
        #base_element = array[a]
        base_element = array[0]
        print(base_element)
        less = [i for i in array[1:] if i <= base_element]
        print(less)
        greater = [i for i in array[1:] if i > base_element]
        print(greater)
        return quick_sort(less) + [base_element] + quick_sort(greater)

print(quick_sort([10, 8, 5, 44, 24]))