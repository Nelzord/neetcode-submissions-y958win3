class Solution:

    def findDeflection(self, nums, l, r):
        if l == r: 
            return nums[l]

        mid = (l + r) // 2



        if nums[mid] > nums[r]:
            l = mid + 1
            return self.findDeflection(nums, l, r)
        else:
            r = mid
            return self.findDeflection(nums, l, r)


    def findMin(self, nums: List[int]) -> int:
        #do a binary search. find the element that is less than its previous one 
        return self.findDeflection(nums, 0, len(nums) - 1)