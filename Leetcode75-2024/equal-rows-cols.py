class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        n = len(grid)
        keyDict = {}

        for i in grid:
            tempStr = ""
            for j in i:
                tempStr += str(j) + "0"
            if keyDict.get(tempStr) == None:
                keyDict[tempStr] = 1
            else:
                keyDict[tempStr] += 1

        indX, indY = 0, 0
        count = 0
        for indX in range(n):
            tempStr = ""
            for indY in range(n):
                tempStr += str(grid[indY][indX]) + "0"
            if keyDict.get(tempStr) == None:
                continue
            else:
                # keyDict[tempStr] += 1
                count += keyDict.get(tempStr)


        print keyDict, count

        return count
