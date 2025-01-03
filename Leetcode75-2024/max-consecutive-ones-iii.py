class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        n = len(nums)
        count_zero = 0 if nums[0] == 1 else 1
        start, end = 0, 0
        maxCon = 0

        while(end < n):
            while (count_zero <= k and end < n):
                end += 1
                if end < n and not(nums[end]):
                    count_zero += 1
            
            maxCon = max(maxCon, end-start)

            while (count_zero > k and start < n):
                if start < n and not(nums[start]):
                    count_zero -= 1
                start += 1
        
        return maxCon


