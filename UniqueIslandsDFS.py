class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        def depthFirstSearch(r, c):
            if 0 <= r < rows and 0 <= c < cols and (r, c) not in seen and grid[r][c] == 1:
                seen.add((r, c))
                path_direction.append((r - origin_row, c - origin_col))
                depthFirstSearch(r+1, c)
                depthFirstSearch(r-1, c)
                depthFirstSearch(r, c+1)
                depthFirstSearch(r, c-1)
        
        seen = set()
        unique_path = set()
        
        for r in range(rows):
            for c in range(cols):
                path_direction = []
                origin_row = r
                origin_col = c
                depthFirstSearch(r, c)
                if path_direction:
                    unique_path.add(tuple(path_direction))
        
        return len(unique_path)
