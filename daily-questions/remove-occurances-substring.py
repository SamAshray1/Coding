class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        # temp = s.replace(part, "")
        # print temp, s
        # temp = s.replace(part, "")
        # print temp

        while len(s) != 0:
            temp = s.replace(part, "")
            if temp == s:
                break
            else:
                s = temp
        return s
        