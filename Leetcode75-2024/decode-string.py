class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []
        currStr = ""
        currNum = 0
        prevStr = ""
        for i in s:
            if i.isdigit():
                currNum = currNum*10 + int(i)
            elif i == "[":
                stack.append(currStr)
                stack.append(currNum)
                currStr = ""
                currNum = 0
            elif i == "]":
                num = stack.pop()
                prevStr = stack.pop()
                currStr = prevStr + currStr*num
            else:
                currStr += i

            print(stack, currStr, currNum)
        
        return currStr
                
