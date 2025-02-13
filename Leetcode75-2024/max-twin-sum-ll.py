# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        head1 = ListNode(val=0, next=head)
        slow, fast = head1, head1

        while fast.next != None:

            fast = fast.next.next
            if not fast and fast.next != None:
                break
            slow = slow.next

        secondHead = slow.next
        secondCurr = secondHead
        newNode = ListNode(0, next=None)

        while secondCurr != None:
            newCurr = ListNode(secondCurr.val, next=None)
            newCurr.next = newNode
            secondCurr = secondCurr.next
            newNode = newCurr

        maxSum = 0
        curr = head
        secondCurr = newNode
        while curr != secondHead and secondCurr.next != None:
            maxSum = max(curr.val + secondCurr.val, maxSum)
            curr = curr.next
            secondCurr = secondCurr.next
        
        return maxSum
