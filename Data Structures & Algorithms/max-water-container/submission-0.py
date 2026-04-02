class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #two pointer left and right -> greedily take the higher next container edge
        # -> keep track of max water


        maxWater = 0

        lPtr = 0
        rPtr = len(heights) - 1

        while lPtr <= rPtr:
            maxWater = max(maxWater, (rPtr - lPtr) * min(heights[rPtr], heights[lPtr]))

            if heights[lPtr] > heights[rPtr]:
                rPtr -= 1
            elif heights[lPtr] < heights[rPtr]:
                lPtr += 1
            else: 
                rPtr -= 1
                lPtr += 1
        return maxWater

