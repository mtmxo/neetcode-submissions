class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for j in nums:
            count[j] = count.get(j, 0) + 1
        
        for j, i in count.items():
            if i > len(nums)//2:
                return j 