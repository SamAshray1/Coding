class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        length1 = len(word1)
        length2 = len(word2)

        index1, index2 = 0,0
        final_string = ''
        while True:
            
            if index1 < length1:
                # print(word1[index1])
                final_string += word1[index1]
            
            if index2 < length2:
                # print(word2[index2])
                final_string += word2[index2]
            if index1 < length1:
                index1+=1
            if index2 < length2:
                index2+=1
                
            # print(final_string)
            if index1 >= length1 and index2 >= length2:
                break

        print('"'+final_string+'"')
        return final_string