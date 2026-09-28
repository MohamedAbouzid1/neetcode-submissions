class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i, x = 0, len(numbers) -1

        while i < x:
            currSum = numbers[i] + numbers[x]
            if currSum > target:
                x -= 1
            elif currSum < target:
                i += 1
            else:
                return [i+1, x+1]
        return []