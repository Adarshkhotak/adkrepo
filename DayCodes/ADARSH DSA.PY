char = "Hhj438&*&$*#(     AHWUuda121&*(^$#*&))"
cap_count =0
small_count =0
for ch in char:
    ascii_code = ord(ch)
    if ascii_code >= 65 and ascii_code <=90:
     cap_count +=1

    elif ascii_code >= 97 and ascii_code<=122:
      small_count +=1
print(cap_count)
print(small_count)
