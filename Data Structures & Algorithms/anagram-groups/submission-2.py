class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            keys = [0] * 26
            for char in word:
                keys[ord(char) - ord("a")] += 1
            
            res[tuple(keys)].append(word)   

        return list(res.values())
