# NeetCode Products of Array Except Self (https://neetcode.io/problems/products-of-array-discluding-self?list=neetcode150)
# Calculate all the left products for each index and store them in answer array. Then calculate all the right products in reverse 
# order and multiply them with the left products in the answer array.

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer
    
sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))  # Output: [24,12,8,6]