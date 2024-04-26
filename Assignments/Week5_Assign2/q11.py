'''Given a dictionary with key-value pairs, remove all the keys with
values greater than K, including mixed values.
Input : test_dict = {‘Gfg’ : 3, ‘is’ : 7, ‘best’ : 10, ‘for’ : 6, ‘xyzx’ : ‘CS’}, K = 7
Output : {‘Gfg’ : 3, ‘for’ : 6, ‘xyzx’ : ‘CS’}'''

from typing import Dict


def removeKeys(dictionary: Dict, K1: int):
    # Uncomment this, if you want to change in original dictionary
    dictt = dictionary.copy()

    keys_to_remove=[] #it takes keys whose value is freater thn 7 in nxt forloop pop them.
    for k,v in dictt.items():
        if type(v)== int and v>K1:
            keys_to_remove.append(k)
    
    for key in keys_to_remove:
        dictt.pop(key)
    return dictt

test_dict2 = {"Gfg": 3, "is": 7, "best": 10, "for": 6, "qqqq": "CS"}
K1 = 7

print(removeKeys(test_dict2,K1))