class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        subDict = {}
        numOps = 0

        for i in nums:
            if subDict.get(i) != None and subDict[i] > 0:
                subDict[i] = subDict[i] - 1
                numOps += 1
                continue

            else:
                subtracted = k - i
                if subDict.get(subtracted) != None:
                    subDict[subtracted] = subDict[subtracted] + 1
                else:
                    subDict[subtracted] = 1
            # print(subDict)
        
        return numOps
        