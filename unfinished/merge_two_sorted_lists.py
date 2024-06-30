# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1:ListNode, list2:ListNode):
        if list1 is None and list2 is None:
            return(None)
        elif list1 is None: 
            return(list2)
        elif list2 is None: 
            return(list1)
        
        if list1.val < list2.val:
            a = list1 
            b = list2 
            returned = list1 
        else:
            a = list2 
            b = list1
            returned = list2
        # 1 2 4 
        # 1 3 4
        # 1 1 2 3 4 4

        while a is not None and b is not None: 
            a_next = a.next # None
            b_current = ListNode(b.val, b.next) # 2 
            if a_next is None and b_current is not None:
                a.next = b
                break
            # print(a_next.val, b_current.val)
            # if a_next is not None:
            if a_next.val < b.val:
                a = a.next
            else: 
                b_current.next = a_next 
                a.next = b_current 
                a = a.next 
                b = b.next 
            # # elif b.next is not None:
            # else:
            #     break
        return(returned)
    
l1 = ListNode(1, ListNode(2, ListNode(4, None)))
l2 = ListNode(1, ListNode(3, ListNode(4, None)))
l3 = ListNode(2, None)
l4 = ListNode(1, ListNode(3, None))

if __name__ == "__main__":
    a = Solution().mergeTwoLists(l3, l4)
    # while a:
    #     print(a.val)
    #     a = a.next