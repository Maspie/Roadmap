class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        result = []    
        for point in points:
            dist = point[0]**2 + point[1]**2
            res.append((dist, point[0], point[1]))

        heapq.heapify(res)

        while k > 0:
            d, x, y = heapq.heappop(res)
            result.append([x,y])
            k-=1

        
        return result

        




        