#inp= ["tea","ate","eta","pos","sop"]

def make_dict(inp):
    res={}
    seen=inp[0]
    for i in range(1,len(inp)):
            if sorted(seen)==sorted(inp[i]):
                if seen not in res:
                    res[seen]= [inp[i]]
                else:
                     res[seen].append(inp[i])
            else:
                seen=inp[i]
    return res

print(make_dict(["tea","ate","eta","pos","sop"]))

'''Finding All Anagrams in a String.
from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)
#defaultdict with list as This means that if a key is not present in the dictionary, it will automatically create an empty list for that key.   
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    
    result = {}
    for key, value in anagrams.items():
        if len(value) > 1:
            result[value[0]] = value[1:]
    
    return result'''


'''
def find_anagrams_simple(s, p):
    p_sorted = ''.join(sorted(p))  # Step 1: Sort the string p
    p_len = len(p)
    result = []

    for i in range(len(s) - p_len + 1):  # Step 2: Iterate through substrings of s
        if ''.join(sorted(s[i:i + p_len])) == p_sorted:  # Step 3: Sort and compare
            result.append(i)
    
    return result

# Example usage
s = "cbaebabacd"
p = "abc"
print(find_anagrams_simple(s, p))  # Output: [0, 6]'''




'''
from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    return list(anagrams.values())

# Example usage
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]'''

#Valid Email Adresses
def is_valid_email(email: str) -> bool:
    # Check if '@' is present exactly once
    if email.count('@') != 1:
        return False
    
    # Split into local part and domain
    local, domain = email.split('@')
    
    # Local part and domain must not be empty
    if not local or not domain:
        return False
    
    # Domain must contain at least one dot
    if '.' not in domain:
        return False
    
    # Split domain into name and extension
    domain_name, *extensions = domain.split('.')
    
    # Domain name and extension must not be empty
    if not domain_name or not all(extensions):
        return False
    
    # Extension should be at least 2 characters (like com, org, in)
    if any(len(ext) < 2 for ext in extensions):
        return False
    
    return True


# Example usage
emails = [
    "test@example.com",
    "user.name@domain.co.in",
    "invalid-email@",
    "another.test@domain.org",
    "wrong@domain",
    "@missinglocal.com",
    "missingdomain@.com"
]

valid_emails = [email for email in emails if is_valid_email(email)]
print("Valid emails:", valid_emails)

#OR
import re

def is_valid_email(email: str) -> bool:
    # Regex pattern for validating email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
