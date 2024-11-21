# Could have used two pointers for better complexity

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        vowelList = ['a', 'e', 'i', 'o', 'u']
        vowelEncountered = []

        for i in s:
            if i.lower() in vowelList:
                vowelEncountered.append(i)
        
        vowelEncountered = vowelEncountered[::-1]
        print(vowelEncountered)
        reverseStr = ""
        for i in s:
            if i.lower() in vowelList:
                reverseStr += vowelEncountered[0]
                vowelEncountered.pop(0)
            else:
                reverseStr += i

        return reverseStr