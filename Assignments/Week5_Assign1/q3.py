'''Make a dictionary with keys as subject name (physics, chemistry, etc.)
and values as their marks. Print the name of the subject which has marks
more than passing marks (above 33)'''
from typing import Dict
my_dict : Dict[str,int] ={"Physics":86 ,"Maths":96,"Chemistry":80,"Bio":70, "CS":33,"Marathi":30,}

for sub, mark in my_dict.items():
    if mark >=33:
        print( sub,mark)