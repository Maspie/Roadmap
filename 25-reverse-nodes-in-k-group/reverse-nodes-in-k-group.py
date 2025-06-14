# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def kth(curr, k):

            while curr and k > 0:
                curr = curr.next
                k -=1
            return curr

        dummy = ListNode(0, head)
        groupprev = dummy

        while True:

            last = kth(groupprev, k)
            if not last:
                break

            #saving last's next value so we know
            groupnex = last.next

            #reversing, need 2 -  prev = None (ideally) but not in this case, curr 
            prev = groupnex # prev will not be None as we need to connect it later
            curr = groupprev.next
            while curr != groupnex:

                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                
            # connecting the reversed list
            tmp = groupprev.next
            groupprev.next = last
            groupprev = tmp

        return dummy.next