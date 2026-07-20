class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        verify = set()
        for i in nums:
            if i in verify:
                return True
            else:
                verify.add(i)
        return False