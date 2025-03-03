# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxLength = 0
        def solve(node, deep, dir):
            self.maxLength = max(self.maxLength, deep)

            if node.left is not None:
                solve(node.left, deep+1,'left') if dir != 'left' else solve(node.left, 1, 'left')
            if node.right is not None:
                solve(node.right, deep+1, 'right') if dir != 'right' else solve(node.right, 1, 'right')
        solve(root, 0, '')
        return self.maxLength
