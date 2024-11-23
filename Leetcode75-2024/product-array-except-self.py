class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lenNum = len(nums)

        preffix = [0]*lenNum
        suffix = [0]*lenNum
        # print(suffix)

        preffix[0] = 1
        suffix[lenNum-1] = 1

        for i in range (1, lenNum):
            preffix[i] = preffix[i-1] * nums[i-1]
        # print(preffix)  
        
        for i in range(lenNum-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        # print(suffix)

        for i in range(lenNum):
            nums[i] = preffix[i] * suffix[i]

        return nums
