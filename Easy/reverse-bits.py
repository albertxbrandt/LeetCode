# NeetCode Reverse Bits (https://neetcode.io/problems/reverse-bits?list=neetcode150)
# Thought process: The problem is to reverse the bits of a given 32 bits unsigned integer.
# To achieve this, we can iterate through each of the 32 bits of the integer.
# We check if each is 0 or 1 and then set the corresponding bit in the result integer at the reversed position.

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            if ((n >> i) & 1) == 1:
                result |= (1 << (31 - i))
        return result