# Problem: NeetCode Single Number (https://neetcode.io/problems/single-number?list=neetcode150)
# Thought Process: For every number that appears twice they need to be cancelled out. Leaving a single number not cancelled out.

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0 # Store result of XOR operation
        for num in nums:
            result ^= num # Use XOR to cancel out numbers appearing twice because it goes by the bits
        return result
    
sol = Solution()
print(sol.singleNumber([2,2,1,5,5,6,6]))  # Output: 1
print(sol.singleNumber([60,5,3,5,60]))  # Output: 3