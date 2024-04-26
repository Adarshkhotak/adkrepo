'''Write a Python program to combine two dictionary by adding values
for common keys.'''
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3={}
for k,v in d1.items():
    if k in d2:
        d3[k]=d1[k]+d2[k]
    else:
        d3[k]=d1[k]
        #d3[k]=d2[k]  
for k,v in d2.items():
    if k not in d1:
        d3[k]=d2[k]

print(d3)  

'''OPTIMAL WAY
def combineDictionary1(d1, d2):
    combined_dict = {}

    # This combines keys of both d1 and d2
    for key in d1.keys() | d2.keys():
        combined_dict[key] = d1.get(key, 0) + d2.get(key, 0)

    return combined_dict'''

