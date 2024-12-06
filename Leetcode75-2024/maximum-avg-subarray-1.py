class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        maxSum = 0
        for i in range(k):
            maxSum += nums[i]
        
        currSum = maxSum
        for i in range(k, len(nums)):
            currSum += nums[i] - nums[i-k]

            maxSum = max(currSum, maxSum)

        return maxSum / float(k) 
