class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s): return 0

        #define variables
        p1, p2 = 0, 0 
        maxLength = 1
        valid = True
        numOccurances = dict()
        numOccurances[s[p1]] = 1

        #main loop
        while not p2 == len(s) - 1 or not valid:
            #if valid move right pointer
            if valid:
                p2 += 1
                if s[p2] not in numOccurances or numOccurances[s[p2]] == 0: numOccurances[s[p2]] = 1
                else:
                    numOccurances[s[p2]] += 1
                    valid = False
            #if invalid move left pointer
            else:
                numOccurances[s[p1]] -= 1
                if numOccurances[s[p1]] == 1:
                    valid = True
                p1 += 1
            #if valid see if greater than max length
            if valid: maxLength = max(maxLength, p2-p1+1)
        
        return maxLength

s = Solution()
print(s.lengthOfLongestSubstring("bbbbb"))