'''Q2. Make a dictionary with keys as subject name (physics, chemistry, etc.)
and values as their marks. Print the name of the subject with highest marks
scored'''
from typing import Dict

my_dict : Dict[str,int] ={"Physics":86 ,"Maths":96,"Chemistry":80,"Bio":70, }
Highest =0
HM_sub =""
for sub , marks in my_dict.items(): 
    if marks>Highest:
        Highest=marks
        HM_sub = sub
print(f"{HM_sub} has Highest marks {Highest}")
    