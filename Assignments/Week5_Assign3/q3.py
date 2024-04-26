'''Here’s a student data with name, age, city, total marks.
Sort this list according to total marks and print it'''
student_data = [
["Samantha", 18, "New York", 420], #-->x so x[3] marks
["David", 25, "Los Angeles", 380],
["Sophie", 22, "Chicago", 390],
["Michael", 20, "Houston", 410],
["Liam", 19, "Phoenix", 430],
["Olivia", 21, "Philadelphia", 400],
["Daniel", 23, "San Antonio", 375],
]
sort_list =sorted(student_data , key=lambda x:x[3])
print(sort_list)