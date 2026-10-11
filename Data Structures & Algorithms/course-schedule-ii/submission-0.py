class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # hashmap course : prerequisites

        hashmap = { i: [] for i in range(numCourses) }
        for course, prereq in prerequisites:
            hashmap[course].append(prereq)
        visited = set()
        path = set()
        res = []

        def dfs(course, path):
            # base case
            if course in path:
                return False
            if course in visited:
                return True
            
            path.add(course)
            for prereq in hashmap[course]:
                if dfs(prereq, path) == False:
                    return False
            path.remove(course)
            visited.add(course)
            res.append(course)
        
        for course in hashmap:
            if dfs(course, path) == False:
                return []
        
        return res
        

