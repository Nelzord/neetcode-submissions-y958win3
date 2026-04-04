class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def bfs(r, c):
            
            directions = [[1,0],[0,-1],[0,1],[-1,0]]
            for d in directions:
                x = r + d[0]
                y = c + d[1]
                if 0 <= x < len(heights) and 0 <= y < len(heights[0]):
                    if heights[x][y] >= heights[r][c] and (x,y) not in visited:
                        print('can flow from', [r,c], [x,y])
                        visited.add((x,y))
                        bfs(x,y)
            return visited


        resultList = []
        pacific = set()
        atlantic = set()
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                    visited = set()         
                    visited.add((i,j))   
                    if i == 0 or j == 0:
                        pacific.update(bfs(i,j))
                    if i == len(heights) - 1 or j == len(heights[0]) - 1:
                        atlantic.update(bfs(i,j))
                        
        print(pacific, atlantic)
        resultSet = pacific & atlantic
        print(resultSet)
        return [[x, y] for (x, y) in resultSet]

