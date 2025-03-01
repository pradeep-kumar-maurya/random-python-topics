# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ The idea is to use tortoise and hare approach """
        temp_head = head
        node = head
        count = 0

        while node is not None:
            count += 1
            node = node.next

        upperbound = (count // 2) + 1
        i = 1

        while i < upperbound:
            temp_head = temp_head.next
            i += 1

        return temp_head


s = Solution()
node = s.middleNode(l1)
print(node.val)



