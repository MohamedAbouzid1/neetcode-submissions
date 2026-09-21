class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = nums
        
        i = 0
        while i < n:
            ans.append(nums[i])
            i += 1

        return ans