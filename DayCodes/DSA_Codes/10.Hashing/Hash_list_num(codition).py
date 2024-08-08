'''
ls=[5,8,3,1,5,1,1,3,8,7,6,5]
#codition is list elements are b/w 1 to 8 only so we need 9 index positions only

hash_list=[0]*9  #created a list index o to 8 by stting value as 0
for i in range(len(ls)):
    hash_list[ls[i]]+=1
print(hash_list)

n=int(input("Enter a number want to count:"))
print(hash_list[n])'''

arr=[5,8,3,1,5,1,1,3,8,7,6,5]
#codition is list elements are b/w 1 to 8 only so we need 9 index positions only

hash_list=[0]*9  #created a list index o to 8 by stting value as 0
for i in arr:
    hash_list[i]+=1
print(hash_list)

n=int(input("Enter a number want to count:"))
print(hash_list[n])