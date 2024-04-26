'''Write a function that takes a dictionary and a key, and returns True if
the key is found in the dictionary, otherwise False'''
def key_exist(d,key):
    if key in d:
        return True
    return False 
my_dict = {"name": "Anirudh", "age": 56, "gender": "Male"}
print(key_exist(my_dict,"age"))