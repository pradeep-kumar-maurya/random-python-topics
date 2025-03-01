from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:

        final_value = 0

        for operation in operations:
            if operation[1] == '+':
                final_value += 1
            elif operation[1] == '-':
                final_value -= 1

        return final_value


s = Solution()
print(s.finalValueAfterOperations(["X++","++X","--X","X--"]))

