'''Store name as a Key, and 5 marks in a List as a value in dictionary.
Store details of at least 5 students. Print the total marks with percentage
of each and every student'''
def student_marks():
    students = {
        "Alice": [95, 85, 90, 88, 93],
        "Bob": [75, 80, 78, 72, 70],
        "Charlie": [88, 90, 92, 85, 87],
        "Daisy": [65, 70, 68, 64, 67],
        "Ethan": [55, 57, 60, 58, 55],
    }
    results = {}
    for name, marks in students.items():
        total=0  #total = sum(marks) -->we can use this also instead of below for loop
        for i in marks:
            total=total+i
            
            percentage = total / 5
        print(f"Name = {name}, total = {total}, percentage = {percentage:.2f}")
student_marks()