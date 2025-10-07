# Neetcode Number-Of-One-Bits (https://neetcode.io/problems/number-of-one-bits?list=neetcode150)
# Thought Process: I wanted to iterate through all of the 32 bits and compare each to 1, if they are equal then add to count.
# I started off by trying to just make the n integer a string so i could just iterate through but str(n) converted the number to decimal.
# Then after trying multiple different things I viewed the hint which suggested using range(32) to iterate through all the bits and then I got
# shifted bits to the right by i and compared it to 1 using the & operator. Then added to count if it was equal to 1.

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0 # Track the count of 1's
        for i in range(32): # loop through 32 times because there are 32 bits being given in the input
            count += (n >> i) & 1 # get the right most bit and compare it to 1, if it is 1 then it will add to the count.
        return count