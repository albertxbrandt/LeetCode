# NeetCode Longest Substring Without Duplicates (https://neetcode.io/problems/longest-substring-without-duplicates?list=neetcode150)
# Thought process: We need to find the longest substring without repeating characters.
# We can use a sliding window approach with two pointers, left and right. Time complexity is o(n^3). Will try for optimal later.
# Version 2 of this solution, first version didn't work, this version is slow.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_length = 0
        l = 0
        r = 0

        if len(s) == 1:
            return 1

        while r < len(s):
            if s[r] not in seen:
                seen[s[r]] = r
                r += 1
            else:
                max_length = max(max_length, len(s[l:r]))
                l = seen[s[r]] + 1
                r = seen[s[r]] + 1
                seen = {}

            max_length = max(max_length, len(s[l:r]))

        return max_length

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(sol.lengthOfLongestSubstring("thequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsovert")) # Output: 17