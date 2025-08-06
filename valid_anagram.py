class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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

solution = Solution()


# Teste
s = 'arturz'
t = 'arthru'
resultado1 = solution.isAnagram(s,t)
s2 = 'listen'
t2 = 'silent'
resultado2 = solution.isAnagram(s2,t2)

print(resultado1)
print(resultado2)

