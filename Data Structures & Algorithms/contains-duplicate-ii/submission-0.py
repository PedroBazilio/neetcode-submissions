class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numsSet = {}
        left = 0
        
        for r in range(len(nums)):
            if nums[r] in numsSet and r - numsSet[nums[r]] <= k:
                return True
            numsSet[nums[r]] = r
        return False        