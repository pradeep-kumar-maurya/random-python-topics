from collections import defaultdict
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq_dict = defaultdict(list)

        for i in range(len(nums)):
            freq_dict[nums[i]].append(i)

        total_pairs = 0

        for value in freq_dict.values():
            n = len(value) - 1
            if len(value) > 1:
                total_pairs += (n * (n + 1)) // 2  # formula for sum of nos from 1 to n

        return total_pairs

s = Solution()

print(s.numIdenticalPairs([1,2,3]))
