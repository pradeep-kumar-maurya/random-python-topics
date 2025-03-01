from typing import List


class Solution:
    def removeDuplicates(self, A: List[int]) -> int:
        index = 0

        for i in range(len(A)):
            if A[index] != A[i]:
                index += 1
                A[index] = A[i]

        return index + 1


s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
