class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
        maxAlt = 0
        alt = 0
        for i in gain:
            alt = alt + i
            maxAlt = max(maxAlt, alt)
            
        return maxAlt