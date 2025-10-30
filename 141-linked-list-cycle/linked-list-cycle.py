class Solution(object):
    def hasCycle(self, head):
        #pointers intialization
        slow = head
        fast = head
        #iterating through the loop
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False        