'''Here’s student data.'''
student_data = {
"Ella": {"age": 20, "marks": [85, 78, 92, 89, 91]},  # it is dict in dict for q4 dict in dict in list
"Max": {"age": 22, "marks": [79, 85, 88, 90, 87]},
"Sophia": {"age": 21, "marks": [92, 95, 88, 85, 91]},
"Liam": {"age": 23, "marks": [76, 80, 79, 82, 85]},
"Ava": {"age": 20, "marks": [88, 92, 85, 90, 87]},
"Noah": {"age": 22, "marks": [83, 85, 80, 86, 88]},
"Emma": {"age": 21, "marks": [90, 87, 92, 88, 86]},
}
'''
for v in student_data.values():
    for k,v2 in v.items(): #v is value dict which of main student_data dict
        if type(v2)==list:
            tm =sum(v2)
            v[k]=tm
#print(student_data) o/p-->{'Ella': {'age': 20, 'marks': 435}, 'Max': {'age': 22, 'marks': 429},

#sort_dict = sorted(student_data.items())
#o/p-->[('Ava', {'age': 20, 'marks': 442}), ('Ella', {'age': 20, 'marks': 435}),
sort_dict = sorted(student_data.items(),key=lambda x:x[1]["marks"])
#print(sort_dict)  #op is in list only not converted to dict

for i in sort_dict:
    print(f"{i[0]} has scored {i[1]['marks']}") '''
#Optimal Method
my_dict={}
for k,v in student_data.items():
    my_dict[k]=sum(v["marks"])

sort_my_dict =dict(sorted(my_dict.items(),key=lambda x:x[1]))

for k,v in sort_my_dict.items():
    print(f"{k} has scored {v} marks")

    
