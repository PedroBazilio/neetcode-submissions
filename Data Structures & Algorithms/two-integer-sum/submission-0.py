class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        var = {}
        n = len(nums)
        for i in range(n):
            complement = target - nums[i]
            if complement in var:
                return [var[complement], i]
            else:
                var[nums[i]] = i
                print(var)
        return []
