'''Given two dictionaries, write a function to merge them into a new
dictionary. If there is any overlap of keys, the value from the second
dictionary should overwrite the one from the first dictionary'''
'''
dict1 ={'apple': 3, 'banana': 5, 'cherry': 7}
dict2= {'banana': 8, 'orange': 10, 'apple': 9}
dict1.update(dict2)  #it is used to add as well as it uodates i.e overwrites value also
print(dict1)'''
def merge_dictionaries2(d1, d2):
    #merged = d1.copy()  # Start with a copy of the first dictionary
    for key, value in d2.items():
        d1[key] = (
            value  # Set the value from the second dictionary, overwriting if key exists
        )
    return d1


print(
    merge_dictionaries2(
        {"apple": 3, "banana": 5, "cherry": 7},
        {"banana": 8, "orange": 10, "apple": 9},
    )
)
