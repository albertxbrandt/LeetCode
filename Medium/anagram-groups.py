# Neetcode Anagram Groups (https://neetcode.io/problems/anagram-groups?list=neetcode150)
# Thought process: We need to group words that are anagrams of each other.
# To solve this we can use a hash map where the key is a representation of the
# char counts of the word nd the value is a list of words that match that character count.

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = {} 
        for word in strs:
            count = [0] * 26
            
            for c in word:
                count[ord(c) - ord("a")] += 1
            
            key = tuple(count)
           
            if key not in res:
                res[key] = [] 
            
            res[key].append(word)

        return list(res.values())

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]