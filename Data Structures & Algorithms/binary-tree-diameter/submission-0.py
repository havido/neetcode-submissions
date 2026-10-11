# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # depth
        # at intersection, does sum of 2 children > max? replace maxSum if yes
        if not root:
            return 0
        maxSum = 0
        def dfs(node):
            nonlocal maxSum
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if left + right > maxSum:
                maxSum = left + right
            return max(left, right) + 1
        dfs(root)
        return maxSum