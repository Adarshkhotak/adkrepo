def swapcase(string):
    result = ""
    for ch in string:
        ascii_code = ord(ch)
        if ascii_code >= 65 and ascii_code <= 90:
            ascii_code = ascii_code + 32 # we need to add 32 in ascii value of capital to make them small letters ascii value. 
            new_char = chr(ascii_code) #chr() is used to convert ascii value to character value.
            result += new_char
        elif ascii_code >= 97 and ascii_code <= 122:
            ascii_code = ascii_code - 32
            new_char = chr(ascii_code)
            result += new_char
        else:
            result += ch
    return result
a = "ANIruDh$#^*   !@@#@000ADWKAhhdkwa   ___++"
print(swapcase(a))
        