class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def in_order(self, root):
        if root is None:
            return

        self.in_order(root.left)
        print(root.val, end=' ')
        self.in_order(root.right)

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t7 = TreeNode(7)

t1.left = t2
t1.right = t5
t2.left = t3
t2.right = t4
t5.right = t6
t6.right = t7
