class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """

        rList = []
        dList = [] 
        n = len(senate)   
        for i in range(0,n):
            if senate[i] == "R":
                rList.append(i)
            else:
                dList.append(i)
        
        while len(rList) != 0 and len(dList) != 0:
            rPop = rList.pop(0)
            dPop = dList.pop(0)
            if rPop < dPop:
                rList.append(n)
            else:
                dList.append(n)
            n+=1
        
        # print(rList, dList)
        if len(rList) == 0:
            return "Dire"
        else:
            return "Radiant"
            
