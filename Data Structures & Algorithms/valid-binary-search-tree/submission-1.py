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
        res = []
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            res.append(node.val)
            inOrder(node.right)
        inOrder(root)
        for i in range(1, len(res)):
            if res[i] <= res[i-1]:
                return False
        return True
