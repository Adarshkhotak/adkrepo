my_list = ["abc", "y", 12, 55.55, "python", "qzr"]
#result = "".join(my_list)
#result = "z".join(i for i in my_list) #it is also add z to each element of list
result = "".join(str(i) for i in my_list)
print(result)
