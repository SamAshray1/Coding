# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global count
        count = 0

        def preTraversal(node, maxi):
            if not node:
                return 

            global count

            if maxi <= node.val:
                count += 1
                maxi = node.val
            
            # print node.val, maxi, count
            
            preTraversal(node.left, maxi)
            preTraversal(node.right, maxi)


        preTraversal(root, root.val)
        # print count        
        return count

