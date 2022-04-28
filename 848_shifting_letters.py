def shiftingLetters(s, shifts) -> str:
    res = list(s)
    
    for i in range(len(s)):
        j = 0
        while j <= i:
            res[j] = chr(ord(res[j]) + (shifts[i]%26))
            j += 1
    
    return ''.join(res)

print(shiftingLetters("abc", [3, 5, 9]))

# class Solution:
#     def findlargest(x):
#         maxVal = float("-inf")
#         maxValIndex = -1
#         for i, val in enumerate(x):
#             if val > maxVal:
#                 maxVal = val
#                 maxValIndex = i
#         del x[maxValIndex]
#         return maxVal
        
    
#     def conneg(x):
#         for i,j in enumerate(x):
#             if j<0:
#                 x[i]=j*-1
                
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         sol = ['']*len(nums)
        
#         conneg(nums)
        
#         for i in range(len(nums)-1,0,-1):
#             sol[i] = findlargest(nums)**2
        
#         return sol