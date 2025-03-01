from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        f_num = nums[0]
        for num in nums:
            if num != f_num:
                break
        else:
            return f_num

        sum1 = 0
        sum2 = 0

        for i in range(1, len(nums), 1):
            sum1 += i

        for num in nums:
            sum2 += num

        return sum2 - sum1


s = Solution()
print(s.findDuplicate([1,4,4,2,4]))
