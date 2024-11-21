class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        canPlant = 0
        lenFlower = len(flowerbed)
        for i in range(0, lenFlower):
            if (flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == lenFlower-1 or flowerbed[i+1] == 0)):
                flowerbed[i] = 1
                canPlant += 1
            
            
        if canPlant >= n:
            print(canPlant)
            return True
        else:
            return False
        