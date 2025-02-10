# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None:
            return None
        newList = ListNode(val=head.val, next=None)
        curr = head

        while curr.next != None:
            curr = curr.next

            newNode = ListNode(val=curr.val, next=newList)
            newList = newNode
        
        return newList 