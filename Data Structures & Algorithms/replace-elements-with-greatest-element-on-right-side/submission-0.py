class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0] * len(arr)
        right_max = -1

        for j in range(len(arr)-1, -1, -1):
            ans[j] = right_max
            right_max = max(arr[j], right_max)

        return ans