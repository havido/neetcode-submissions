# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder is level by level, root -> left -> right
        # inorder is left -> root -> right

        hashmap = { inorder[i]: i for i in range(len(inorder)) }
        rootIndex = 0

        def dfs(l, r):
            nonlocal rootIndex
            if l > r:
                return None
            rootVal = preorder[rootIndex]
            rootIndex += 1
            root = TreeNode(rootVal)
            mid = hashmap[rootVal]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root

        return dfs(0, len(inorder) - 1)
            


    

