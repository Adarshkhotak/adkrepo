''' Ask a string from user. Store the frequency of each character in the
dictionary. Then print the character with the maximum frequency'''
string =input("Enter a string:")
mydict ={}
for ch in string:
    if ch in mydict:
        mydict[ch] +=1
    else:
        mydict[ch]=1

High =0
for k,v in mydict.items():
    if v>High:
        High=v
        char=k

print(f"Max frequent character is {char}")

