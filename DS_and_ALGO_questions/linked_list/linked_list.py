class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


l1 = ListNode(10)
head = l1
node = l1
l2 = ListNode(20)
l3 = ListNode(30)

l1.next = l2
l2.next = l3

while node is not None:
    print(node.value)
    node = node.next

print("head value", head.value)
# print(node.value)  # node is now pointing to None
