# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head)
        start = front 
        while start != None: 
            prefixSum = 0 
            end = start.next 
            while end != None: 
                prefixSum += end.val 
                if prefixSum == 0: 
                    start.next = end.next 
                end = end.next 
            start = start.next 
        return(front.next)