# Gets the level order of tree, then append the last element which is the rightmost element to a list and return it. 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
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
        result = []
        for i in self.res:
            result.append(i[-1])
        return result