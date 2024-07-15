class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowlen = len(grid)
        collen = len(grid[0])
        visited = set()
        count = 0

        def dfs(row, col):
            nonlocal count
            if 0 <= row < rowlen and 0 <= col < collen and (row, col) not in visited and grid[row][col] == '1':
                visited.add((row, col))
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)

        for row in range(rowlen):
            for col in range(collen):
                if grid[row][col] == '1' and (row, col) not in visited:
                    dfs(row, col)
                    count += 1

        return count
