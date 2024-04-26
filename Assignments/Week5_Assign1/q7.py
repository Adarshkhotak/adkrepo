'''Python program to find the size of a Dictionary. Basically print how
many total key-value pair are there.'''
from typing import Dict
my_dict : Dict[str,int] ={"Physics":86 ,"Maths":96,"Chemistry":80,"Bio":70, }
count =0
for i in my_dict.keys():
    count+=1
print(count)