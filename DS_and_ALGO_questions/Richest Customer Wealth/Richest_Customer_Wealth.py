from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        sum = 0
        for i in accounts:
            for j in i:
                sum += j
            if sum > max:
                max = sum
            sum = 0

        return max


s = Solution()
print(s.maximumWealth([[1, 2, 3], [3, 2, 1]]))
