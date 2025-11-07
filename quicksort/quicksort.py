from random import randrange
def qsort(array):
    if len(array)<2:        
        return array
    else:
        pivot = array.pop(randrange(len(array)))        
        small = [i for i in array if i<=pivot]
        big = [i for i in array if i>pivot]
        return qsort(small) + [pivot] + qsort(big)
