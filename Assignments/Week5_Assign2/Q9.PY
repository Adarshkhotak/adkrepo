'''Write a Python program to create a dictionary of keys x, y, and z where
each key has as value a list from 11-20, 21-30, and 31-40 respectively.
Access the fifth value of each key from the dictionary'''
# You can create dictionary like this too
data = {
    "x": list(range(11, 20)),
    "y": list(range(21, 30)),
    "z": list(range(31, 40)),
}

for key, value in data.items():
    print(value[4]) #Value is list so we can indexing on it