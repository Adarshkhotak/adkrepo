'''Here’s a student data. The first 3 elements are marks of student. Sort
this list and print it.'''
student_data = [
[78, 92, 85, "Alice"],
[82, 79, 81, "Bob"],
[92, 88, 85, "Charlie"],
[80, 79, 82, "Diana"],
[92, 85, 90, "Eva"],
[85, 80, 86, "Frank"],
[87, 92, 88, "Gina"]
]

dict1={}
for x in student_data:
    dict1[x[-1]]=sum(x[:3])

sort_dict= dict(sorted(dict1.items(),key=lambda x: x[1]))
print(sort_dict)

for k,v in sort_dict.items():
    print(f"{k} has scored {v} marks")
    



    
        
    
        
           
