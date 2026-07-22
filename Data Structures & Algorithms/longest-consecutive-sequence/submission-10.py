class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res = 0
        
        var = set(nums)

        for num in var:
            if (num - 1) not in var:
                length = 1
                while (num + length) in var:
                    length +=1 

                res = max(res, length)


        return res