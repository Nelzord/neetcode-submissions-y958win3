class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort list
        #left point and right pointer -> index through middle list
        # [-3, -1, 0, 1, 2, 3, 4]


        result = []
        nums.sort()

        for lPtr in range(len(nums) - 2):
            if lPtr > 0 and nums[lPtr] == nums[lPtr - 1]:
                continue
            
            mIdx = lPtr + 1
            rPtr = len(nums) - 1

            while mIdx < rPtr:
                total = nums[lPtr] + nums[mIdx] + nums[rPtr]

                if total == 0:
                    res = [nums[lPtr], nums[mIdx], nums[rPtr]]
                    result.append(sorted(res))
                    mIdx += 1
                    rPtr -= 1

                    while mIdx < rPtr and nums[mIdx] == nums[mIdx - 1]:
                        mIdx += 1
                    while mIdx < rPtr and nums[mIdx] == nums[rPtr + 1]:
                        rPtr -= 1

                elif total < 0:
                    mIdx += 1
                else:
                    rPtr -= 1
        return result    

