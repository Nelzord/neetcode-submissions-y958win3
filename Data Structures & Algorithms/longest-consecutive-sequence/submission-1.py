class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #have a hashmap of all seen elements prev
        #add the value and the current num
        #find the highest value of the map


        nums.sort()
        highestVal = 0
        seen = {}
        for i in nums:
            if i - 1 in seen.keys():
                val = seen[i - 1] + 1
                seen[i] = val
                highestVal = max(val, highestVal)
            else:
                seen[i] = 1
                highestVal = max(highestVal, 1)
        return highestVal