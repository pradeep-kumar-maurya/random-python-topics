from typing import Optional
from Tree_creation import TreeNode

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

# print(t1.in_order(t1))

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        self.depth = 0
        def check_max_depth(root):
            if root is None:
                return
            else:
                self.depth += 1

            check_max_depth(root.left)
            check_max_depth(root.right)
            if self.depth > self.max:
                self.max = self.depth

            # this is very important because once we finish a node we move up and therefore we reduce depth by 1
            self.depth -= 1

        check_max_depth(root)
        return self.max

        '''
        OR
        if root is None:
            return 0
    
        # The idea is to just find the (max btw left tree and right tree + 1)   
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        '''

s = Solution()
print(s.maxDepth(t1))
