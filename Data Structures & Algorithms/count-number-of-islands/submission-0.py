class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i,j):
            q = deque() 
            q.append([i, j])

            while q:
                cords = q.pop() 
                x = cords[0] 
                y = cords[1] 
                grid[x][y] = "0" 
                directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

                for d in directions:
                    if 0 <= x + d[0] < len(grid) and 0 <= y + d[1] < len(grid[0]) and grid[x + d[0]][y + d[1]] == "1": 
                        q.append([x + d[0], y + d[1]])

            return


    
        numIslands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    grid[i][j] == "0"
                    numIslands += 1
                    bfs(i, j)
        return numIslands