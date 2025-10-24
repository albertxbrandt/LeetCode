# NeetCode Is Palindrome (https://neetcode.io/problems/is-palindrome?list=neetcode150)
# Thought Process: We can use two pointers, one starting at the beginning and one at the end of the string.
# We move the pointers towards each other, skipping non-alphanumeric characters. When the characters at both pointers are alphanumeric,
# we compare them in a case-insensitive manner. If they don't match, we return False. If the pointers cross each other, we return True.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l <= r:
            if not s[l].isalnum():
                l += 1
                continue

            if not s[r].isalnum():
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        return True
    
sol = Solution()
print(sol.isPalindrome("Was a car? a rac a saw!")) # Output: True