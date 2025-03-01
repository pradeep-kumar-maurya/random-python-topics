class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True

        if n & (n - 1) == 0:
            return True

        return False


s = Solution()
print(s.isPowerOfTwo(6))
