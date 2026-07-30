class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tam = len(nums)
        res,pref,suf = [0] * tam, [1] * tam, [1] * tam
        print(pref)
        
        for i in range(1,tam):
            pref[i] = nums[i -1] * pref[i-1]

        for i in range(tam-2, -1, -1):
            suf[i] = nums[i+1] * suf[i + 1]

        for i in range(tam):
            res[i] = pref[i] * suf[i]
        
            

        return res