'''
Created on May 8, 2016

@author: ray.wang
'''

def remove_smallest(numbers):
    # raise NotImplementedError("TODO: remove_smallest")
    
    if numbers:
        numbers.remove(min(numbers))
    
    return numbers
    
    
if __name__ == '__main__':
    
    # remove_smallest
    
    # works for the examples
    assert(remove_smallest([1, 2, 3, 4, 5]) == [2, 3, 4, 5])
    assert(remove_smallest([5, 3, 2, 1, 4]) == [5, 3, 2, 4])
    assert(remove_smallest([1, 2, 3, 1, 1]) == [2, 3, 1, 1])
    assert(remove_smallest([]) == [])
    
    from numpy.random import randint
    
    def randlist():
        return list(randint(400, size=randint(1, 10)))
    
    # returns [] if list has only one element
    for i in range(10):
        x = randint(1, 400)
        assert(remove_smallest([x]) == [])
        
    # returns a list that misses only one element
    for i in range(10):
        arr = randlist()
        assert(len(remove_smallest(arr[:])) == len(arr) - 1)
