'''Write a Python script to print a dictionary where the keys are numbers
between 1 and 15 (both included) and the values are squares of the keys'''
my_dict=dict()
for i in range(1,16):
    my_dict[i]=i**2
    #my_dict[values]=i**2
print(my_dict)