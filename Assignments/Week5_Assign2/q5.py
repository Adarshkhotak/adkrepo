'''Given a dictionary, write a function that returns a new dictionary
containing only the keys that have values of type str'''
#method 1 
'''
def del_str(d):
    res ={}
    for k, v in d.items():
        if type(v)== str:
            res[k] = v #don't give == this throws error
            

    return res'''
#method 2
def del_str(d):
    return {k:v for k,v in d.items() if  isinstance(v,str)} # dict comprehenssion
        

my_dict = {"name":"Adarsh","Age":23,"City":"Pune","Is_student":False,"State":"Karnataka"}
print(del_str(my_dict))
