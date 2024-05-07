class Solution:    
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Doubles the node and gives carry
        def twice(head):
            if not head:
                return 0            
            doubled_value = head.val * 2 + twice(head.next)
            head.val = doubled_value % 10
            return doubled_value // 10
        
        carry = twice(head)
        if carry:
            head = ListNode(carry, head)
        return head