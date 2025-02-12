# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def preOrderTraversal(node, listA):
            if not node:
                return 
            elif node.left == None and node.right == None:
                # print(node.val)
                listA.append(node.val)
                
            preOrderTraversal(node.left, listA)
            preOrderTraversal(node.right, listA)
            return listA
        
        listA = preOrderTraversal(root1, [])
        # print(listA)
        listB = preOrderTraversal(root2, [])

        if listA == listB:
            return True
        else:
            return False