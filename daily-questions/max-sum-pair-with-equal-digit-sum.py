class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # Get the sum of digits of an element and add the index to a dictionary
        # sumDict = {}

        # for i in range(len(nums)):
        #     sum = 0
        #     tempNum = nums[i]
        #     while tempNum != 0:
        #         digit = tempNum % 10
        #         sum += digit
        #         tempNum = tempNum / 10
            
        #     if sumDict.get(sum):
        #         sumDict[sum].append(i)
        #     else:
        #         sumDict[sum] = [i]

        # # print sumDict
        # maxSum = -1

        # for value in sumDict.values():
        #     if len(value) <= 1:
        #         continue
        #     else:
        #         for indI in range(len(value)):
        #             for indJ in range(indI):
        #                 # print(nums[value[indI]] + nums[value[indJ]])
        #                 loopSum = nums[value[indI]] + nums[value[indJ]]
        #                 maxSum = max(loopSum, maxSum)
        # return maxSum

        maxArr = [0]*82
        ans = -1
        for i in range(len(nums)):
            sum = 0
            tempNum = nums[i]
            while tempNum != 0:
                digit = tempNum % 10
                sum += digit
                tempNum = tempNum / 10

            if maxArr[sum] != 0:
                ans = max(maxArr[sum]+nums[i], ans)

            maxArr[sum] = max(maxArr[sum], nums[i])

        return ans