class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        i, j = 0, len(height)-1
        maxArea = 0

        while i != j:
            mini = min(height[i], height[j])
            area = mini*(j-i)

            if area > maxArea:
                maxArea = area
            
            if mini == height[i]:
                i = i+1
            else:
                j = j-1

        return maxArea