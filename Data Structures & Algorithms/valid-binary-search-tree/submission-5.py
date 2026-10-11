# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # # in order traversal O(n) time with O(1) space complexity
        # if not root or (not root.left and not root.right):
        #     return True
        # prev = -1001
        # def inOrder(node) -> bool:
        #     nonlocal prev
        #     if not node:
        #         return True
        #     if not inOrder(node.left):
        #         return False
        #     if node.val <= prev:
        #         return False
        #     prev = node.val
        #     return inOrder(node.right)
        
        # return inOrder(root)

        # top down dfs with localMin and localMax
        def dfs(node, localMin, localMax):
            if not node:
                return True
            if not localMin < node.val < localMax:
                return False
            return dfs(node.left, localMin, node.val) and dfs(node.right, node.val, localMax)

        return dfs(root, float('-inf'), float('inf'))
