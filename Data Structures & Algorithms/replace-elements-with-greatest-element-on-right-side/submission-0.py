class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        ans = [0] * len(arr)
        for i in range(len(arr) -1, -1, -1):
            print(arr)
            
            ans[i] = rightMax
            rightMax = max(arr[i], rightMax)

        return ans