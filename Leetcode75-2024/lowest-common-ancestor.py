# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        return l or r

        # self.internal = False
        # def searchInternal(node1, node2):
        #     if not node1:
        #         return
        #     if node1.val == node2.val:
        #         self.internal = True
        #         return
            
        #     searchInternal(node1.left, node2)
        #     searchInternal(node1.right, node2)

        #     return self.internal
        
        # if searchInternal(p, q):
        #     return p
        # self.internal = False
        # if searchInternal(q, p):
        #     return q

        # self.found = []
        # self.found1 = False
        # self.found2 = False
        # def traverse(node, node1, node2):
        #     if not node:
        #         self.found.append(node)
        #         return

        #     self.found.append(node.val)
        #     if node.val == node1.val:
        #         self.found1 = True
        #     elif node.val == node2.val:
        #         self.found2 = True
            
        #     if self.found1 and self.found2:
        #         return
            
        #     traverse(node.left, node1, node2)
        #     traverse(node.right, node1, node2)
        
        # traverse(root, p, q)
        # print self.found