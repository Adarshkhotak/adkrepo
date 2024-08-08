st="ansjdhyudhsscc"#only samll ttl 26 characters

hash_li=[0]*26

for ch in st:
    index=ord(ch)-97 #97 is ascii value of 'a' satrat
    hash_li[index]+=1

n=input("Enter a ch want to count:")
print(hash_li[ord(n)-97])