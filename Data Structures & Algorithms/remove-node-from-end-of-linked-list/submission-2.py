# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        idx = 0
        ref = head
        prev = None

        temp = head
        lenList = 0
        #find length
        while temp:
            lenList += 1
            temp = temp.next

        while head:
            if idx == (lenList - n):
            
                if prev is None:
                    return head.next
                prev.next = head.next
                return ref

            prev = head
            head = head.next
            idx = idx + 1

        return ref