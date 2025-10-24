# NeetCode Two Integer Sum II (https://neetcode.io/problems/two-integer-sum-ii?list=neetcode150)
# Thought Process: Since the input array is sorted we can use two pointers, one at the beginning and one at the end.
# We calculate the sum of the two pointers, if it matches the target we return the indices.
# If the sum is less than the target we move the left pointer to the right to increase the sum.
# If the sum is greater than the target we move the right pointer to the left to decrease the sum.
# Add 1 to each index before returning since the problem states the indices are not zero based.

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            total = numbers[l] + numbers[r]

            if total == target:
                return [l + 1, r + 1]

            if total < target:
                l += 1
            elif total > target:
                r -= 1

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))  # Output: [1,2]