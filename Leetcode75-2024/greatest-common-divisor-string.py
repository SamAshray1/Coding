class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len1 = len(str1)
        len2 = len(str2)

        if str1 + str2 == str2 + str1:

            minLen = len1 if len1 < len2 else len2
            gcd = 1
            for i in range(1,(minLen+1)):
                if len1%i == 0 and len2%i == 0:
                    gcd = i
                else:
                    continue
            
            return str1[:gcd]

        else:
            return ""
            
            