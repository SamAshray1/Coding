class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # numsLen = len(nums)
        # pivot = -1
        # leftSum, rightSum = [], []

        # for i in range(numsLen):
        #     sum = 0
        #     for j in range(0,i):
        #         sum += nums[j]
        #     leftSum.append(sum)
            
        #     sum = 0
        #     for j in range(i+1, numsLen):
        #         sum += nums[j]
        #     rightSum.append(sum)
        
        # for i in range(numsLen):
        #     if leftSum[i] == rightSum[i]:
        #         pivot = i
        #         break
        
        # return pivot

        numsLen = len(nums)
        pivot = -1
        leftSum, rightSum = 0, sum(nums)
 

        for i in range(0, numsLen):
            rightSum -= nums[i]
            if leftSum == rightSum:
                pivot = i
                break
            leftSum += nums[i]
            
            print leftSum, rightSum, i

        return pivot
        