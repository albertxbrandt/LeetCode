# NeetCode Permutation in String (https://neetcode.io/problems/permutation-string?list=neetcode150)
# Thought process: Using a sliding window of size len(s1) and slide over s2 checking if the sorted substring matches the sorted s1.
# If we find a match return True, otherwise False after checking all substrings. This is not the most optimal solution but it is pretty
# straightforward. 

# Will work on a more optimal solution later.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        for l in range(len(s2) - len(s1) + 1):
            r = l + len(s1)
            sl1 = sorted(s1)
            sub = sorted(s2[l:r])
            if sl1 == sub:
                return True

        return False
    
sol = Solution()
print(sol.checkInclusion("ab", "eidbaooo"))  # True