class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(si, ei):
            if si > ei:
                return True
            
            while si < ei:
                if s[si] != s[ei]:
                    return False
                
                si += 1
                ei -= 1
                
            return True
        
        si = 0
        ei = len(s)-1
        
        while si < ei:
            if s[si] != s[ei]:
                return checkPalindrome(si+1, ei) or checkPalindrome(si, ei-1)
            
            si += 1
            ei -= 1
        
        return True
            