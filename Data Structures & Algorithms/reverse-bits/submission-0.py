class Solution:
    def reverseBits(self, n: int) -> int:

        ans = 0

        for _ in range(32):

            # Make space for the next bit
            ans <<= 1

            # Copy the last bit of n into ans
            ans |= (n & 1)

            # Remove the last bit from n
            n >>= 1

        return ans