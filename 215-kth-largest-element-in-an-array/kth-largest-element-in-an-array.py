class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)

            else:
                if num < heap[0]:
                    continue
                else:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)

        return heap[0]

        kth = []
        i = 0
        while i > k:
        
            heapq.push(kth, nums[i])
                