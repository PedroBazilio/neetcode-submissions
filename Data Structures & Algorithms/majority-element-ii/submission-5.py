class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        arr = {}
        res = []
        print(res)
        for i in range(len(nums)):
            arr[nums[i]] = arr.get(nums[i], 0) + 1

            if (arr[nums[i]] > len(nums) // 3) and nums[i] not in res:
                res.append(nums[i])
        
        return res