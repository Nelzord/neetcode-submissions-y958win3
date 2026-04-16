class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        minValToBeat = len(nums) / 3
        res = []
        stor = {}

        for i in nums:
            if i in stor.keys():
                stor[i] += 1
            else:
                stor[i] = 1

        for i in stor.keys():
            if stor[i] > minValToBeat:                    
                res.append(i)
        
        return res
        
        