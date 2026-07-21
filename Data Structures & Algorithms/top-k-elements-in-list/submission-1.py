class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums ) + 1)]

        n = len(nums)
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            #adiciono na posicao do count o numero 
            freq[cnt].append(num)
        res = []
        print(freq)
        for i in range(len(freq) - 1, 0, -1):
            for num in (freq[i]):
                print(num)
                res.append(num)
                if len(res) == k:
                    return res
