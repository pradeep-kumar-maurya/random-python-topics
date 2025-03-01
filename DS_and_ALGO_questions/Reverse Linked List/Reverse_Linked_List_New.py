# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        This logic takes the 1st node and then point it to None.
        Then takes the 2nd node and point it to the 1st node and so on.
        Linked list will be reversed.
        '''

        if head is None:
            return None

        temp_head = head.next
        previous_node = head
        previous_node.next = None

        while temp_head is not None:
            dummy_head = temp_head
            temp_head = temp_head.next
            dummy_head.next = previous_node
            previous_node = dummy_head

        return previous_node


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

s = Solution()
head = s.reverseList(l1)

while head is not None:
    print(head.val, end=' ')
    head = head.next



