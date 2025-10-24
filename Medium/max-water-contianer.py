# NeetCode Max Water Container (https://neetcode.io/problems/max-water-container?list=neetcode150)
# Thought process: We need to find two heights that can contain the most water. As we move closer our width decreases.
# We can use two pointers, left and right and move the pointer with the small height inward to try and find a taller height. 
# We can store max area each loop iteration. After the loop is over we return the max result.

class Solution:
    def maxArea(self, heights: list[int]) -> int:
        res = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            res = max(res, (r - l) * min(heights[l], heights[r]))
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1

        return res

sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49