from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        '''
        We need to use modulus operator and some mathematical concept in order to retrieve back the orginial no.
        '''
        n = len(nums) + 1
        for i in range(len(nums)):
            if nums[nums[i]] < n:
                nums[i] = nums[i] + nums[nums[i]] * n
            else:
                nums[i] = nums[i] + (nums[nums[i]] % n) * n

        for i in range(len(nums)):
            nums[i] = nums[i] // n

        return nums


s = Solution()

a = [0,2,1,5,3,4]
print(s.buildArray(a))
