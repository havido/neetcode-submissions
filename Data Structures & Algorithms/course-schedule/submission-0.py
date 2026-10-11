class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # if len(visited) == numCourses
        # hashmap: course -> [prereqs]
        # if cycle exists -> impossible
        hashmap = {i: [] for i in range(numCourses)}
        visited = set()
        path = set()

        for course, prereq in prerequisites:
            hashmap[course].append(prereq)
        
        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            path.add(course)
            for pr in hashmap[course]:
                if not dfs(pr):
                    return False
            path.remove(course)
            visited.add(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True