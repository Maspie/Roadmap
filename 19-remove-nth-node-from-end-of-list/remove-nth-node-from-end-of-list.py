# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # #reversing the list

        # curr = head
        # prev = None

        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        # dummy = ListNode(0, prev)
        # curr = dummy

        # for _ in range(n-1):
        #     curr = curr.next

        # curr.next = curr.next.next
        # if dummy.next is None:
        #     return None

        # curr = dummy.next
        # prev = None

        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp



        # return prev
            
       

        #slow fast pointer
        dummy = ListNode(0, head)
        slow = fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next if slow.next else None

        return dummy.next

        

        