'''
Merge k sorted linked lists and return it as one sorted list. 
Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        '''recursive'''
        def merge_2_lists(list1, list2):
            '''in place linear sort

            O(n) - where n is items in 2 lists
            '''
            previous = ListNode(-1)
            start = previous
            while list1 and list2:
                if list1.val <= list2.val:
                    previous.next = list1
                    list1 = list1.next
                else:
                    previous.next = list2
                    list2 = list2.next
                previous = previous.next

            previous.next = list1 if list1 else list2

            return start.next

        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        # k is number of lists
        # O(logK) - total complexity = O(nlogK) 
        # recursion adds space complexity
        mid = len(lists)//2
        return merge_2_lists(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:]))

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        '''Iterative Solution''' 
        def merge_2_lists(list1, list2):
            previous = ListNode(-1)
            start = previous
            while list1 and list2:
                if list1.val <= list2.val:
                    previous.next = list1
                    list1 = list1.next
                else:
                    previous.next = list2
                    list2 = list2.next
                previous = previous.next

            previous.next = list1 if list1 else list2

            return start.next

        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        while len(lists) > 1:
            pairs = len(lists) // 2
            # no ceil function - so add 1 for odd numbers 
            if len(lists) % 2 != 0:
                pairs += 1

            index, i = 0, 0
            while index < pairs:
                if i+1 < len(lists):
                    # store merged results of pairs in first k/2 indexes
                    lists[index] = merge_2_lists(lists[i], lists[i+1])
                else:
                    # handle the odd case 
                    lists[index] = lists[i]
                i = i + 2
                index += 1
            # remove rest of the list
            lists = lists[:pairs]

        return lists[0]
