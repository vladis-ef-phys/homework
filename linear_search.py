def linear_search(list, key):
    n = len(list)
    for i in range(0, n):
        if (list[i] == key):
            return i
    return -1

list = [1, 3, 5, 4, 7, 9]
key = 1
if(linear_search(list, key) == -1):
    print('Element not found')
else:
    print('Element index:', linear_search(list, key))