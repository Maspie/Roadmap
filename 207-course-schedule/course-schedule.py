class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {}
        for i in range(numCourses):
            premap[i] = []

        for c, p in prerequisites:
            premap[c].append(p)

        visit = set()

        def dfs(c):
            if c in visit:
                return False
            if premap[c] == []:
                return True
            visit.add(c)
            for pre in premap[c]:
                if not dfs(pre):
                    return False

            visit.remove(c)

            premap[c] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True