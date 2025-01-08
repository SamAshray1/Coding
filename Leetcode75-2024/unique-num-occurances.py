class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freqDict = {}

        for i in arr:
            if freqDict.get(i) == None:
                freqDict[i] = 1
            else:
                freqDict[i] += 1
        print(freqDict)

        occFreqDict = {}
        for i in freqDict.keys():
            if occFreqDict.get(freqDict[i]) == None:
                occFreqDict[freqDict[i]] = 1
            else:
                occFreqDict[freqDict[i]] += 1

        print(occFreqDict)

        for i in occFreqDict.values():
            if i > 1:
                return False
                break
        return True