# Neetcode Counting Bits (https://neetcode.io/problems/counting-bits?list=neetcode150)
# Thought process: This was similar to the previous problem of counting the number of bits of
# an integer. The only difference is now I need to do it for every number 0 to n and return a list
# of the counts.
class Solution:
    def countBits(self, n: int) -> list[int]:
        results = [] # Store the results of counts for each number
        for i in range(n + 1): # Loop through every number from 0 to n (inclusive)
            count = 0 # Track the count of 1's for the current number
            num = i # Store the current number to manipulate
            while num:
                count += num & 1 # Get the right most bit and compre to 1, if it is 1 then it will add to the count.
                num >>= 1 # Shift the bits to the right to check the next bit.
            results.append(count) # Append the count for the current number to results
        return results
    
sol = Solution()
print(sol.countBits(4))  # Output: [0,1,1,2,1]