st="ydvdgtshadarshkhiotddAA# #"
hash_dict={}
for ch in st:
    hash_dict[ch]=hash_dict.get(ch,0)+1

c=input("Enter a ch want to count:")
print(hash_dict[c])
