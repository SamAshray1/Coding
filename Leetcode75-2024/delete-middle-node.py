# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head.next:
            return None

        itera, iteraFast = head, head
        while iteraFast.next != None:

            iteraFast = iteraFast.next.next

            if not iteraFast or iteraFast.next == None :
                itera.next = itera.next.next
                print "here"
                break

            itera = itera.next

            # print(itera.val, " ", iteraFast.val)

        return head