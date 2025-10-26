# WIP: Longest Substring Without Duplicates
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_length = 0
        count = 0
        for i, c in enumerate(s):
            if c in seen and i - 1 == seen[c]:
                max_length = max(max_length, count)
                count = 1
                seen = {c: i}
                continue
            if c not in seen:
                seen[c] = i
                count += 1
            else:
                max_length = max(max_length, count)
                seen[c] = i
                count = len(seen) - 1
            print(seen)

        return max(max_length, len(seen))
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
