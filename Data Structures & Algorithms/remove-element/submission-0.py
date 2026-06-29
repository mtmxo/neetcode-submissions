class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow_p = 0
    
        for fast_p in range(0, len(nums)):
            
            if nums[fast_p] != val:
                nums[slow_p] = nums[fast_p]
                slow_p += 1
            
        return slow_p