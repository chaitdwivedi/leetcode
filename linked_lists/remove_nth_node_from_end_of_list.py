'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # add dummy to start
        # to handle removal of first element
        dummy = ListNode(-1)
        dummy.next = head
        ptr, ptr_n = dummy, head
        
        # move ptr_n n steps ahead 
        while n > 0:
            ptr_n = ptr_n.next
            n = n - 1
        
        # take ptr_n to end 
        # that means ptr's next will be nth from end
        while ptr_n:
            ptr = ptr.next
            ptr_n = ptr_n.next 
        
        # delete
        ptr.next = ptr.next.next
        return dummy.next
