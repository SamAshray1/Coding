class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []
        for i in s:
            stack.append(i)
            if i == "*":
                stack.pop()
                stack.pop()
        
        return ''.join(stack)