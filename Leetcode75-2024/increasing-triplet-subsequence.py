class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        lenNums = len(nums)

        if lenNums < 3:
            return False

        minimum, secondmin = float('inf'), float('inf')
        # for i in nums:
        #     if i <= minimum:
        #         minimum = i
        #     elif i <= secondmin:
        #         secondmin = i
        #     else:
        #         return True
        
        # return False
        
        for i in nums:
            if i < minimum:
                minimum = i
                # secondmin = minimum
            
            elif i > minimum and i < secondmin:
                secondmin = i
            
            elif i > minimum and i > secondmin:
                return True
        return False


        
        
            