class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])

        visited = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def backtrack(cur, r, c):
            
            
            cur += board[r][c]

            if not word.startswith(cur):
                return False
            
            
            #print(cur)

            if cur == word:
                return True

            for d in directions:
                x = d[1] + c
                y = d[0] + r
                if 0 <= x < cols and 0 <= y < rows and (y,x) not in visited:
                    #backtrack("", y, x)
                    visited.add((y,x))
                    if backtrack(cur, y, x):
                        return True
                    visited.remove((y,x))
            return False


        for i in range(cols):
            for j in range(rows):
                visited.add((j,i))
                if backtrack("", j, i):
                    return True
                visited.remove((j,i))
        return False

        