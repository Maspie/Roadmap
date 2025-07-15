class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {}

        for i in range(numCourses):
            premap[i] = []

        for c, p in prerequisites:
            premap[c].append(p)

        cycle = set()
        visit = set()
        output = []

        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True

            cycle.add(c)
            for pre in premap[c]:
                if dfs(pre) == False:
                    return False

            cycle.remove(c)
            visit.add(c)
            output.append(c)
                
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return output
        