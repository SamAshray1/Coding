class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        max = 0
        for i in candies:
            if i > max:
                max = i
        
        returnlist = []
        for i in candies:
            if i + extraCandies >= max:
                returnlist.append(True)
            else:
                returnlist.append(False)
        return returnlist
        