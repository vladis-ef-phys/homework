import random
mass = [[0, ], [1, ], [2, ], [3, ]]
def hash_func(str):
    i = random.randint(0, len(mass)-1)
    if len(mass[i]) == 1:
        mass[i].append(str)
        return mass[i][0]
    else:
        hash_func(str)

print(hash_func(str='abc'))
print(hash_func(str='ab4c'))
print(hash_func(str='ab2c'))
print(hash_func(str='a1bc'))
# mass = [[0, ], [1, ], [2, ], [3, ]]
# mass[0].append('ker')
# print(mass)
