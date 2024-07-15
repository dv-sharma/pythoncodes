from typing import List
from collections import defaultdict

class Solution:
    def pathSum(self, nums: List[int]) -> int:
        # Initialize a dictionary to store node values with (depth, position) as keys
        self.tree = defaultdict(int)
        
        # Parse the three-digit numbers and populate the tree dictionary
        for num in nums:
            depth = num // 100
            position = (num // 10) % 10
            value = num % 10
            self.tree[(depth, position)] = value
        
        # Initialize the total sum of all paths
        self.total_sum = 0

        # Helper function to perform DFS and calculate the path sums
        def dfs(depth, position, current_sum):
            # Calculate the current sum including the current node
            current_sum += self.tree[(depth, position)]
            
            # Determine the positions of the left and right children
            left_child_pos = position * 2 - 1
            right_child_pos = position * 2
            
            # Check if we have reached a leaf node
            if (depth + 1, left_child_pos) not in self.tree and (depth + 1, right_child_pos) not in self.tree:
                self.total_sum += current_sum
                return
            
            # Continue DFS on left and right children if they exist
            if (depth + 1, left_child_pos) in self.tree:
                dfs(depth + 1, left_child_pos, current_sum)
            if (depth + 1, right_child_pos) in self.tree:
                dfs(depth + 1, right_child_pos, current_sum)

        # Start DFS from the root node at depth 1, position 1
        dfs(1, 1, 0)
        
        return self.total_sum
