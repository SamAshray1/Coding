class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word2) > len(word1):
            return False

        set1 = set()
        set2 = set()
        dict1 = {}
        dict2 = {}
        for i in word1:
            set1.add(i)
            if dict1.get(i) == None:
                dict1[i] = 1
            else:
                dict1[i] += 1
        
        for j in word2:
            set2.add(j)
            if dict2.get(j) == None:
                dict2[j] = 1
            else:
                dict2[j] += 1

        if set1.difference(set2):
            return False
        else:
            sortedVal1 = sorted(dict1.values())
            sortedVal2 = sorted(dict2.values())
            for i in range(len(sortedVal1)):
                if sortedVal1[i] == sortedVal2[i]:
                    continue
                else:
                    return False
            return True