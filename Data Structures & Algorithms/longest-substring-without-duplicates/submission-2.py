class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ptr = 0
        
        counter = 0
        res = {}
        for i in range(len(s)):
            if s[i] in res:
                ptr = max(res[s[i]] + 1, ptr)
            res[s[i]] = i
            counter = max(counter,i - ptr + 1)

        return counter
        