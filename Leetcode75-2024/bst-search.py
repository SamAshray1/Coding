# Dont have to recursively go thru all the nodes
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if root and val < root.val:
            return self.searchBST(root.left, val)
        elif root and val > root.val:
            return self.searchBST(root.right, val)
        else:
            return root

        # self.node = None

        # def search(root, val):
        #     if not root:
        #         return 

        #     if root.val == val:
        #         self.node = root

        #     search(root.left, val)
        #     search(root.right, val)
        
        # search(root, val)
        # return self.node

        