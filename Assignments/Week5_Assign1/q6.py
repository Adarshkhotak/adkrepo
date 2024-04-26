'''Write a Python program to check if a dictionary is empty or not'''
from typing import Dict
my_dict : Dict[str,int] ={"Physics":86 ,"Maths":96,"Chemistry":80,"Bio":70, "CS":33,"Marathi":30,}
if len(my_dict)==0:
    print("Dictionary is empty")

print("Not empty") #it automaticakky becomes else 