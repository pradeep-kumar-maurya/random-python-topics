from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_sum = 0
        actual_sum = 0

        for i in range(len(nums) + 1):
            total_sum += i

        for num in nums:
            actual_sum += num

        return total_sum - actual_sum


s = Solution()
print(s.missingNumber([9,6,4,2,3,5,7,0,1]))
