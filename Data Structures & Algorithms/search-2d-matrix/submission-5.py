class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #binary search to find the index of the row the result must be in
        
        cols = len(matrix[0])
        rows = len(matrix)

        l = 0
        r = rows - 1
        
        rowWithResult = None
        while l <= r:
            
            mid = (l + r) // 2
            if matrix[mid][0] < target:
                l = mid + 1
            elif matrix[mid][0] > target: 
                r = mid - 1
            else: 
                return True

        rowWithResult = r


        
        if not (matrix[rowWithResult][0] <= target <= matrix[rowWithResult][cols - 1]):
            return False

        l = 0
        r = cols - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[rowWithResult][mid] < target:
                l = mid + 1
            elif matrix[rowWithResult][mid] > target:
                r = mid - 1
            else:
                return True 

            if mid == (l + r) // 2:
                return False
                
        
        return False

        #binary search to find the val in the range row and return true if found