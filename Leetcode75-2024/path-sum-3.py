# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        self.numPaths = 0
        self.dfs(root, target)

        return self.numPaths

    def dfs(self, node, target):
        if node is None:
            return
        
        self.test(node, target)
        self.dfs(node.left, target)
        self.dfs(node.right, target)

    def test(self, node, target):
        if node is None:
            return
        if node.val == target:
            self.numPaths += 1

        self.test(node.left, target-node.val)
        self.test(node.right, target-node.val)
    
# With memorization
    # def pathSum(self, root, target):
    #     """
    #     :type root: Optional[TreeNode]
    #     :type targetSum: int
    #     :rtype: int
    #     """

    #     self.result = 0
    #     cache = {0:1}

    #     self.dfs(root, target, 0, cache)

    #     return self.result

    # def dfs(self, root, target, currSum, cache):
    #     if root is None:
    #         return
    #     currSum += root.val
    #     oldSum = currSum - target

    #     self.result += cache.get(oldSum, 0)
    #     cache[currSum] = cache.get(currSum, 0) + 1

    #     self.dfs(root.left, target, currSum, cache)
    #     self.dfs(root.right, target, currSum, cache)

    #     cache[currSum] -= 1