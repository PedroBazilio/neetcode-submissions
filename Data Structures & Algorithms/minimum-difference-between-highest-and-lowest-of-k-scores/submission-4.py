class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = k - 1
        minValue = float("inf")
        while r < len(nums):
            minValue = min(minValue, nums[r] - nums[l])
            print(minValue)
            l +=1
            r +=1

        return minValue
        