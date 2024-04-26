'''Q1. Make a dictionary with keys as subject name (physics, chemistry, etc.)
and values as their marks. Print the highest marks scored.'''
from typing import Dict

my_dict : Dict[str,int] ={"Physics":86 ,"Maths":96,"Chemistry":80,"Bio":70, }
Highest =0
for marks in my_dict.values():
    if marks>Highest:
        Highest=marks
print(Highest)

#largest = max(my_dict.values())
#print(largest)



