class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_position: dict[str, int] = {}
        left = 0
        best = 0

        for right, char in enumerate(s):
            if char in last_position and last_position[char] >= left:
                left = last_position[char] + 1

            last_position[char] = right
            best = max(best, right - left + 1)

        return best
        