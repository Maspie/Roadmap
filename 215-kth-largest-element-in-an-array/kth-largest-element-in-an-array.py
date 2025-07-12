class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        num = [-s for s in nums]

        heapq.heapify(num)

        for _ in range(k):
            res = heapq.heappop(num)
        return - 1* res

        
        