# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, currMax):
            nonlocal count
            if not node:
                return
            currMax = max(currMax, node.val)
            if node.val >= currMax: 
                count += 1
            dfs(node.left, currMax)
            dfs(node.right, currMax)
            
        dfs(root, root.val)
        return count