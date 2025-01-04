class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, 0
        n = len(nums)
        maxC = 0
        zeroFlag = 1

        while(end < n):
            if zeroFlag == 1 and nums[end] == 1:
                end += 1
            elif zeroFlag == 1 and nums[end] == 0:
                end += 1
                zeroFlag = 0
            elif zeroFlag == 0 and nums[end] == 1:
                end += 1
            
            elif zeroFlag == 0 and nums[end] == 0:
                if nums[start] == 0:
                    zeroFlag = 1
                start += 1

            maxC = max(maxC, end-start-1)
            
            # print(nums[start:end], zeroFlag)
        return maxC
