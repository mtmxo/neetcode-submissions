class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ris = ""
        min_str = min(strs, key=len)
        for j in range(0, len(min_str)):
            for x in strs:
                if min_str[j] != x[j]:
                    return ris
                
            ris += min_str[j]

        return ris