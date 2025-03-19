import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)

        res = r
        while l <= r:
            
            hours = 0
            mid = (l + r) // 2

            for p in piles:

                hours += math.ceil(float(p)/mid)

            if hours <= h:
                res = min(res, mid)
                r = mid - 1

            else:
                l = mid + 1

        return res

