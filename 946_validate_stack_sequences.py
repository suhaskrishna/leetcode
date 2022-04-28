from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        n = len(pushed)
        j = 0
        for val in pushed:
            st.append(val)
            while len(st) > 0 and j < n and st[-1] == popped[j]:
                st.pop()
                j += 1
        
        return len(st) == 0

            
