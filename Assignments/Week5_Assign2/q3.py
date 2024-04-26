''' Write a function that updates the values of a dictionary by multiplying
them by a given factor only if the value is an integer
FACTOR=2(U may ask from user)'''
def Upd_intvalue(d,fact):
    for k , v in d.items():
        if type(v)==int:
            d[k] = v*fact
    return d
ans =Upd_intvalue({"apple": 3, "banana": 5, "cherry": 7},2)
print(ans)