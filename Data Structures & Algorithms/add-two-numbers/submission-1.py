# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = num2 = 0
        multi = 1
        while l1:
            num1 += l1.val * multi
            multi *= 10
            l1 = l1.next
            
        multi = 1
        while l2:
            num2 += l2.val * multi
            multi *= 10
            l2 = l2.next

        sum_num = num1 + num2

        dummy = ListNode()
        node = dummy
        if sum_num == 0:
            return dummy
        while sum_num >0:
            digit = sum_num % 10
            node.next = ListNode(digit)
            node = node.next
            sum_num //= 10
        return dummy.next

        
        
