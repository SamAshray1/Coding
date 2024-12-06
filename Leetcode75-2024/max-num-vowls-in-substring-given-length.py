class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowl = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        lenS = len(s)
        maxCount = currCount = 0
        
        for i in range(k):
            if vowl.get(s[i]) != None: 
                currCount += 1
        maxCount = currCount

        for i in range(k, lenS):
            if vowl.get(s[i]) != None and vowl.get(s[i-k]) == None:
                currCount += 1
            elif vowl.get(s[i]) == None and vowl.get(s[i-k]) != None:
                currCount -= 1
            
            maxCount = max(currCount, maxCount)
        
        
        return maxCount
