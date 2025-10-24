# NeetCode Three Integer Sum (https://neetcode.io/problems/three-integer-sum?list=neetcode150)
# Thought Process: Sort the input array to make it easier to avoid duplicates and use the two-pointer technique.
# Iterate through the array, fixing one number and using two pointers to find pairs that sum to 0 with the fixed number.
# If the sum of the three numbers is zero, add the triplet to a set to avoid duplicates.
# Convert set to list before returning the result.

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        results = set()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    results.add(tuple([nums[i], nums[l], nums[r]]))
                    l += 1
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1

        return list(results)
    
sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))  # Output: [[-1,-1,2],[-1,0,1]]