class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        max = len(nums)/2
        for i in range(len(nums)):
            res[nums[i]] = res.get(nums[i], 0) + 1

            if res[nums[i]] > max:
                return nums[i]
        