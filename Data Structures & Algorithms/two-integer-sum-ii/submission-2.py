class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n = len(numbers)
        i = 0
        x = n

        while x > i:

            if numbers[i] + numbers[x-1] == target:
                return [i+1, x]
            elif numbers[i] + numbers[x-1] < target:
                i += 1
            else:
                x -= 1
            
