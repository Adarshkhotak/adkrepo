'''A Python dictionary contains List as a value. Write a Python program
to clear the list values in the said dictionary.
'''
my_dict={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}

for k,v in my_dict.items():
    if len(v)>0:
        my_dict[k]=[]
print(my_dict)
#OR
'''for key in my_dict:
        my_dict[key] = []'''