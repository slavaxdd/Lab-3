from random import *
from string import ascii_uppercase

def rand_key():
    AZ = ascii_uppercase
    nums = '0123456789'
    
    key = [''.join(sample(AZ, 3) + [choice(nums)]) for _ in range(4)]
    for part in key:
        #print(part)
        shuffle(list(part))

    #print('-'.join(key))
    return('-'.join(key))

#rand_key()