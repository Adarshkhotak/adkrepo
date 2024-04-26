'''Here’s a students data and their marks.
Display the name of student and total marks in ascending order'''
student_data = {
"Alice": [85, 90, 88, 92, 89],
"Bob": [78, 82, 79, 81, 80],
"Charlie": [92, 95, 88, 85, 91],
"Diana": [76, 80, 79, 82, 85],
"Eva": [88, 92, 85, 90, 87],
"Frank": [83, 85, 80, 86, 88],
"Gina": [90, 87, 92, 88, 86],
}
for k , v in student_data.items():
    student_data[k]=sum(v)
#print(student_data)
#sorting of dictionary
my_dict =sorted(student_data.items() ,key=lambda x:x[1])
my_dict2=dict(my_dict)
for k in my_dict2.keys():
    print(f"{k} has scored {my_dict2[k]} marks")