class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = len(nums)-1
        i=0
        while i != j:
            if nums[i] == 0:
                nums.insert(j+1, 0)
                nums.pop(i)
                j = j - 1
            else:
                i = i + 1
            print(nums, i, j)
        
        return nums