class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))

        dist = {}

        minheap = [[0, k]] # time, startnode

        while minheap:
            time, node = heapq.heappop(minheap)
            if node in dist:
                continue
            dist[node] = time
            

            for nei, t in graph[node]:
                if nei not in dist:
                    heapq.heappush(minheap, (time+t, nei))

        if len(dist) == n:
            return max(dist.values())

        return -1
                


        