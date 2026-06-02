# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first need to find the middle using the 
        #slow and fast pointer technique
        slow = fast = head
        
        while fast.next:
            
            if fast.next:
                if fast.next.next:
                    fast = fast.next.next;
                else:
                    fast = fast.next
            slow = slow.next

        #next need to reverse the second half 
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev=slow
            slow = temp
        

        #now the LL is split into 2 halves
        slow = prev
        temp1,temp2 = head,slow
        dummy = ListNode()
        node = dummy
        flip = 1
        while temp1 and temp2:
            
            if flip == 1 :
                node.next = temp1
                temp1 = temp1.next
                flip -=1
                node = node.next
            elif flip == 0:
                node.next = temp2
                temp2 = temp2.next
                node = node.next
                flip+=1
       
        head = dummy.next
        return None






