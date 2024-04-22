'''string="python is good"
def reversewords(string):
    a=string.split(" ")
    x = a[::-1]
    ans = " ".join(x)
    return ans 

string="python is good"
print(reversewords(string)) 
#op-good is python 
AND '''
def reverse_chars(string:str) -> str:
    return " ".join([i[::-1] for i in string.split()])

string="python is good"
print(reverse_chars(string))
#op-nohtyp si doog

