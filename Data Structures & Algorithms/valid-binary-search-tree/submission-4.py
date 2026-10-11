# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # in order traversal O(n) time with O(n) space complexity
        if not root or (not root.left and not root.right):
            return True
        prev = -1001
        def inOrder(node) -> bool:
            nonlocal prev
            if not node:
                return True
            if not inOrder(node.left):
                return False
            if node.val <= prev:
                return False
            prev = node.val
            return inOrder(node.right)
        
        return inOrder(root)
