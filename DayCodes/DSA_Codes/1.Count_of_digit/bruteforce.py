"""
Time Complexity = O(log10 n) where n is the digit
Space Complexity = O(1)
"""


def count_digits(num: int) -> int:
    count = 0
    n = num
    while n > 0:
        count += 1
        n = n // 10
    return count

--------
print(count_digits(1234))

matrix = [[0] * 3] * 3
matrix[0][0] = 1
print(matrix) #[[1,0,0],[1,0,0],[1,0,0]]

----------
d = {}
d[True] = "Python"
d[1] = "Spark"
print(d)
#{True:"Spark"} (True==1) thats why
-----------
original = [[10, 20], [30, 40]]
copied = original.copy()   #shalow copy for deepcopy copy.deepcopy()
copied[0][0] = 999
copied[1] = [500, 600]
print(original) #[[999,20],[30,40]] 
print(copied) #[[999,20],[500,600]]
-----------

def add_item(item, lst=[]):
    lst.append(item)
    return lst
print(add_item(1)) #[1]
print(add_item(2)) #[1,2]
print(add_item(3, [])) #[3] #new list passed
print(add_item(4)) #[1,2,4] #coz same list
