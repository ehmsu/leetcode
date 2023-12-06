# Definition for singly-linked list.
# import numpy as np 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        l1_list = []
        l2_list = []

        l1_list.insert(0, str(l1.val))
        next_num = l1.next
        while next_num != None:
            l1_list.insert(0, str(next_num.val))
            next_num = next_num.next

        l2_list.insert(0, str(l2.val))
        next_num = l2.next
        while next_num != None:
            l2_list.insert(0, str(next_num.val))
            next_num = next_num.next

        l1 = int(''.join(l1_list))
        l2 = int(''.join(l2_list))

        l3 = reversed(list(l1+l2))
        listnode_l3 = ListNode()
        # listnode_l3.val = l3[0]
        # next_num = listnode_l3.next
        for num in range(len(l3)):
            try:
                listnode_l3.next = ListNode(l3[num])
            except Exception:
                break
            # listnode_l3.val = l3[num]
            
            

        # l3 = reversed(list(str(l1+l2)))
        # l3 = [int(i) for i in l3]

        # return l3

        # print(l1_list)
        # print(l2_list)

