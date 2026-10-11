# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def ddffss(n1, n2):
            if not n1 and not n2:
                return True
            elif n1 and n2 and ddffss(n1.left, n2.left) and ddffss(n1.right, n2.right) and n1.val == n2.val:
                return True
            else:
                return False
        return ddffss(p, q)