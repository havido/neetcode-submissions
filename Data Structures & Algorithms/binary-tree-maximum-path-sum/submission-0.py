# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # max(parent, p+lc, p+rc)
        globalMax = float('-inf')
        
        def dfs(node) -> int:
            nonlocal globalMax
            # base case
            if not node:
                return 0
            # post-order traversal
            leftSum = max(dfs(node.left), 0)
            rightSum = max(dfs(node.right), 0)
            globalMax = max(globalMax, node.val + leftSum + rightSum)
            return node.val + max(leftSum, rightSum)
        dfs(root)
        return globalMax
