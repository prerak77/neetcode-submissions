# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        for i in range(n):
            fast = fast.next
        dummy = ListNode()
        node =dummy
        slow = head
        while True:
            if fast == None:
                node.next = slow.next
                node = node.next
                return dummy.next
            node.next = slow
            slow = slow.next
            fast = fast.next
            node = node.next

