class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers)-1
        res = []
        while l < r:
            if numbers[l] + numbers[r] == target:
                res.append(1+l)
                res.append(1+r)
                return res
            elif numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1

        