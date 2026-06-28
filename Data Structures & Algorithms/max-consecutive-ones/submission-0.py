class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ever = 0
        max_found = 0

        for j in nums:
            if j == 1:
                max_found += 1
            else:
                max_found = 0
            max_ever = max(max_ever, max_found)

        return max_ever
