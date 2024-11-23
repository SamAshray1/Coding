class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        separatedList = s.split()
        lenList = len(separatedList)
        reverseStr = ""

        for ind in range(lenList-1, -1, -1):
            # print separatedList[ind]
            reverseStr += separatedList[ind] + " "
        
        return reverseStr[:-1]