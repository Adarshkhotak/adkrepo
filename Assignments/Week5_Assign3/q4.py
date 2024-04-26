'''Here’s a student data, Sort this data via total marks and print it.'''
student_data = [
{"Sophia": {"age": 21, "marks": [92, 95, 88, 85, 91]}}, # it is dict in dict in list unlike q2.py
{"Max": {"age": 22, "marks": [79, 85, 88, 90, 87]}},
{"Liam": {"age": 23, "marks": [76, 80, 79, 82, 85]}},
{"Ava": {"age": 20, "marks": [88, 92, 85, 90, 87]}},
{"Noah": {"age": 22, "marks": [83, 85, 80, 86, 88]}},
{"Emma": {"age": 21, "marks": [90, 87, 92, 88, 86]}},
{"Olivia": {"age": 24, "marks": [82, 86, 90, 87, 84]}},
]
student_data_temp={}
for x in student_data: #here x is dict now
    for k,v in x.items(): # here v is lat dict i.e {'age': 21, 'marks': [92, 95, 88, 85, 91]}
        student_data_temp[k]=sum(v["marks"]) 
my_dict =sorted(student_data_temp.items(),key=lambda x:x[1])

for k,v in my_dict:
    print(f"{k} has scored {v}marks")

        
                
