class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        minheap = [-s for s in nums]

        heapq.heapify(minheap)

        while k > 1:
            heapq.heappop(minheap)
            k-=1


        return minheap[0] * (-1)