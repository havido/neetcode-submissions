"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}

        # # dfs
        # def dfs(currNode):
        #     # base
        #     if currNode in visited:
        #         return visited[currNode]

        #     clone = Node(currNode.val)
        #     visited[currNode] = clone
        #     # clone.neighbors = []
            
        #     for nb in currNode.neighbors:
        #         clone.neighbors.append(dfs(nb))

        #     return clone
        
        # return dfs(node)

        # =========

        # bfs

        visited[node] = Node(node.val)
        queue = deque([node])

        while queue:
            currNode = queue.popleft()
            for nb in currNode.neighbors:
                if nb not in visited:
                    visited[nb] = Node(nb.val)
                    queue.append(nb)

                visited[currNode].neighbors.append(visited[nb])
        
        return visited[node]
