# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next0 = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        count = 1
        oddNode, evenNode = ListNode(), ListNode()
        oddCurr, evenCurr = oddNode, evenNode
        curr = head
        while curr != None:
            # print curr.val
            if count % 2 == 1:
                oddCurr.next = curr
                oddCurr = oddCurr.next
            else:
                evenCurr.next = curr
                evenCurr = evenCurr.next

            count += 1
            curr = curr.next

        # print oddCurr, evenNode
        evenCurr.next = None
        oddCurr.next = evenNode.next
        return oddNode.next