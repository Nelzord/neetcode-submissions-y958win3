class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #start at beginning -> keep track of unique letters 
        #if a duplicate letter is found, change the start window and reset dict

        curDict = {}
        lPtr = 0
        maxVal = 0
        for i in range(len(s)):
            while s[i] in curDict:
                del curDict[s[lPtr]]
                lPtr += 1
                
            curDict[s[i]] = 0
            maxVal = max(maxVal, i - lPtr + 1)

        return maxVal 