# a = [1, 2, 3, 4, 3, 10, 10]
# passados = []
# duplicados = []

# for elemento in a:
#     if elemento in passados:  
#         if elemento not in duplicados:  
#             duplicados.append(elemento)
#     else:
#         passados.append(elemento)  

# print(duplicados) 

# from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        passados = []
        
        for elemento in nums:
            if elemento in passados:
                return True  
            else:
                passados.append(elemento)
        
        return False  
    

solution = Solution()
resultado = solution.hasDuplicate([1, 2, 3, 1])  
print(resultado)