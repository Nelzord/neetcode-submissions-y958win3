class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        resultList = []
        nums.sort()


        def backtrack(nums, cur):



            if sum(cur) == target:
                resultList.append(cur)
                return 

            if len(nums) == 0:   
                return
                

            if sum(cur) > target:
                return
            
            backtrack(nums, cur + [nums[0]])
            backtrack(nums[1:], cur)

        #go through list 
        backtrack(nums, [])
        return resultList


        