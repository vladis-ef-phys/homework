import time


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None



my_list = [i for i in range(1, 15000000)]

tic = time.perf_counter()
print(binary_search(my_list, 1432592))
toc = time.perf_counter()
print(f"Время {toc - tic:0.4f} секунд")