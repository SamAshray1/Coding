class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        i = 0
        while len(s) != 0 and i < len(s):
            if s[i].isdigit():
                # print(s[i])
                s = s[:i] + s[i+1:]
                i = i - 1
                while i >= 0:
                    if s[i].isalpha():
                        # print(s[i]) 
                        s = s[:i] + s[i+1:] 
                        break
                    i = i-1
            else:
                i += 1
            # print("i", i)
        return s
            