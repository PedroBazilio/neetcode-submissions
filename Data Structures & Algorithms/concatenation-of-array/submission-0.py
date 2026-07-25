class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [0] * (len(nums)) * 2
        count = len(nums)

        for i in range(len(nums)):
            res[i] = nums[i]
            res[count] = nums[i]
            count += 1

        return res
        