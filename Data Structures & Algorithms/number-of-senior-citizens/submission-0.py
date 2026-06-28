class Solution:
    def countSeniors(self, details: List[str]) -> int:
        j = 0
        for x in details:
            if int(x[11:13]) > 60:
                j += 1
        return j