class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ris = []
        for j in words:
            for x in words:
                if j in x and j != x:
                    ris.append(j)
                    break
        return ris