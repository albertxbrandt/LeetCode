# Neetcode Contains Duplicate (https://neetcode.io/problems/duplicate-integer?list=neetcode150)
# Thought process: The problem is to determine if there are any duplicate integers in the given list.
# To solve it we create a set to keep track of the integers we have seen so far and if we encounter one already
# in the set, we can return True. If none then we will return False.

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
        
sol = Solution()
print(sol.hasDuplicate([1,2,3,1]))  # Output: True