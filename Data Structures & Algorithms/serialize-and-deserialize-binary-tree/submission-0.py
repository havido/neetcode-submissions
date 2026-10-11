# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        encoded = ""
        preorder = []

        def dfs(node):
            if not node:
                preorder.append(None)
                return
            preorder.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        for i in range(len(preorder)):
            encoded += str(preorder[i])
            if i != len(preorder) - 1:
                encoded += ','
        
        return encoded
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder = data.split(',')
        preIndex = 0
        
        def dfs():
            nonlocal preIndex
            if preorder[preIndex] == "None":
                preIndex += 1
                return None
            node = TreeNode(int(preorder[preIndex]))
            preIndex += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

