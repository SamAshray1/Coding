# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.res = []

        def levelOrder(root, level, res):
            if not root:
                return
            
            if len(res) <= level:
                self.res.append([])

            self.res[level].append(root.val)

            levelOrder(root.left, level+1, self.res)
            levelOrder(root.right, level+1, self.res)

        levelOrder(root, 0, self.res)
        # print self.res
        
        maxi = float('-inf')
        index = 0
        for i in range(len(self.res)):
            tempSum = sum(self.res[i])
            # print(tempSum)

            if tempSum > maxi:
                index = i +1
                maxi = tempSum
        return index