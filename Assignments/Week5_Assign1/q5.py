'''Write a Python program to generate and print a dictionary that
contains a number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5)'''
my_dict ={}
n=6
for i in range(n):
    my_dict[i]= i*i
print(my_dict)
    
