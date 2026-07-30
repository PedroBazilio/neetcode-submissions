class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        max = len(nums) // 3
        arr = {}
        res = []
        print(res)
        for i in range(len(nums)):
            arr[nums[i]] = arr.get(nums[i], 0) + 1

            if arr[nums[i]] > max and nums[i] not in res:
                res.append(nums[i])
        
        return res