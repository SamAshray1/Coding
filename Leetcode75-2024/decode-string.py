class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []
        currStr = ""
        num = 0
        for i in s:
            if i.isdigit():
                num = num*10 + int(i)
            elif i == "[":
                stack.append(currStr)
                currStr = ""
            elif i == "]":
                currNum = num%10
                num = num/10
                stack.append(currNum*currStr)
                currStr = ""
            else:
                currStr += i

            print(stack, currStr, num)
        
        return stack
                
