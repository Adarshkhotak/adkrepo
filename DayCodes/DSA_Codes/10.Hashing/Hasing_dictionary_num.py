lst = [5, 4, 2, 5, 4, 2, 1, 1, 1, 3, 5, 3]

hash_map = {}

# Pre compute
for num in lst:
    hash_map[num] = hash_map.get(num, 0) + 1 #imp-->here get is used to extract value using key if
    #key is not there in dict we add key to dict and set value as 0 after +1 coz we want to count the value

#print(hash_map)

number = int(input("Enter number to count = "))
print(hash_map.get(number, 0))