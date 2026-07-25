class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in range(len(details)):
            res = list(details[i])
            age = "" + res[11] + res[12]
            print(age)
            if int(age) > 60:
                count +=1


        return count
        