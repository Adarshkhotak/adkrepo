'''Write a Python function that takes a dictionary as input where the
values are lists of integers. The function should return a new dictionary
where the values are lists containing only the even integers from the
original lists'''

def evenlist(d):
    for k,v in d.items():
        ls=[]  
        for i in v:
            if i%2==0:
                ls.append(i)
                d[k]=ls 
    return d 

my_dict ={"A":[1,2,3,4],"B":[5,6,7,8]}
print(evenlist(my_dict))     
    
