# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # helper
        def invert(node):
            temp = node.left
            node.left = node.right
            node.right = temp
        
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            traverse(node.right)
            invert(node)
            return
        traverse(root)
        return root