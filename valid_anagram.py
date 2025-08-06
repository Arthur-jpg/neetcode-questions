def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    count_s = {}
    for char in s:
        if char in count_s:
            count_s[char] += 1
        else:
            count_s[char] = 1
    
    print(count_s)

    for char in t:
        if char in count_s:
            count_s[char] -= 1
        else:
            return False
    print(count_s)
    for count in count_s.values():
        if count != 0:
            return False
    
    return True

# Teste
s = 'arturz'
t = 'arthru'
print(is_anagram(s, t))  # False

s2 = 'listen'
t2 = 'silent'
print(is_anagram(s2, t2))  # True
