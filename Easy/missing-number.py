# NeetCode Missing Numbers (https://neetcode.io/problems/missing-number?list=neetcode150)
# Thought process: The problem is to find the missing number in an array containing distinct numbers from 0 to n.
# My approach was to sort the numbers by increasing order that way i cn loop through the array and compare the index
# to the number at that index, if they are the same then the number is not missing, otherwise if they are different then
# we have found the missing number. This is not the ideal way to solve this problem because I have to sort then iterate through.
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if (i != nums[i]):
                return i
        return len(nums)

sol = Solution()
print(sol.missingNumber([3,0,1])) # Output: 2