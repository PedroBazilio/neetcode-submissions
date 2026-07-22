class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized = [ch.lower() for ch in s if ch.isalnum()]
        left = 0
        right = len(normalized) - 1
        while left < right:
            if  normalized[left] !=  normalized[right]:
                return False
            
            left+=1
            right-=1
        
        return True