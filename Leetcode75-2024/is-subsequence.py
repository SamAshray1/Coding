class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        slen = len(s)
        tlen = len(t)
        i, j = 0, 0
        count = 0

        if slen == 0:
                return True

        while i < slen and j < tlen:
            
            if s[i] == t[j]:
                count += 1
                i += 1
            
            j += 1
            

        return count == slen