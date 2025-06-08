# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        #Find middle node

        slow = fast =  head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        prev = None
        curr = mid
        slow.next = None
        #Reverse second half
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

            

        #now we have two linked list - which start with head and prev respectively
        
        first, second = head, prev

        while second:

            temp_1 = first.next
            temp_2 = second.next
            first.next = second
            second.next = temp_1
            second = temp_2
            first = temp_1
        