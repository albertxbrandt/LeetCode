# HackerRank - Lost Fragments
# Thought process: The problem is to find the words that were sent but not received.
# My approach is to split both sent and received into two seperate lists. Then I will iterate through the sent list
# and compare each word to the current word in the received list. If they match, I will move the pointer in the received list
# forward. If they do not match, I will add the word from the sent list to the result list. If we reach the end of the received list
# then we will add remaining words from the sent list to result list.

class Solution:
    def lostFragments(self, sent, received):
        result = [] # Store lost words here.

        # Split sent and received into lists of words.
        sentList = sent.split(" ")
        receivedList = received.split(" ")

        # Pointer for received list.
        p = 0

        # Loop through sent list and compare to received list.
        for word in sentList:
            if len(receivedList) == p:
                result.append(word)
                continue
            
            if word == receivedList[p]:
                p += 1
            else:
                result.append(word)

        return result
    

sol = Solution()
print(sol.lostFragments("I am sending a secret message", "I am a message")) # Output: ["sending", "secret"]