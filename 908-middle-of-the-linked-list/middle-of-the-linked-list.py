# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        # Step 1: Count total number of nodes
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        # Step 2: Find middle index
        mid = count // 2

        # Step 3: Move again to middle node
        curr = head
        for _ in range(mid):
            curr = curr.next

        return curr
