# Neetcode Two Sum (https://neetcode.io/problems/two-integer-sum?list=neetcode150)
# Thought process: Make a hash map to store the numbers we have seen (as a key) plus their indexes as the value. Check if the
# target - current number exists in the map, if it does then we have found our two numbers that sum to the target.
# Example:
# [ 4, 5, 6 ]
# target: 10

# First loop index 0 (4)
# Check for 10-4 (6)?
# Mone then add 4 map at spot i (0)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif not in seen:
                seen[nums[i]] = i
            else:
                return [seen[dif], i]
            
sol = Solution()
print(sol.twoSum([2,7,11,15], 9))  # Output: [0,1]
