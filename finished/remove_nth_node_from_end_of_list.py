class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get length
        length = 0
        current = head 
        while current: 
            current = current.next 
            length += 1

        # removal 
        counter = 0
        prev = head
        current = head
        if length-n == 0: 
            head = current.next
        else:
            while counter <= (length-n): 
                # print(counter)
                if counter == length-1:
                    prev.next = None
                elif counter == length-n:
                    prev.next = current.next
                    # print("Hello")
                else: 
                    prev = current 
                    current = current.next 
                counter += 1
        return(head)