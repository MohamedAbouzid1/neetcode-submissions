class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

         
        def heapify(nums, size, i):

            largest = i
            left_child = 2* i + 1
            right_child = 2* i + 2

            # if left larger than root
            if left_child < size and nums[left_child] > nums[largest]:
                largest = left_child
            
            # if the right child is the largest so far
            if right_child < size and nums[right_child] > nums[largest]:
                largest = right_child

            # if largest not rood
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]

                heapify(nums, size, largest)

        def buildHeap(nums):
            n = len(nums)

            startIndex = (n // 2) -1
            for i in range(startIndex, -1, -1):
                heapify(nums, n, i)

        buildHeap(nums)

    
        for i in range(len(nums) - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]        
            heapify(nums, i, 0)

        return nums
