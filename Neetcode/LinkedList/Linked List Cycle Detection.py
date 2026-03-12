from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Set T=O(n) S=O(n)
        # visited=set() # to store already visited ListNode
        # cur=head
        # while cur:
        #     if cur in visited:
        #         return True
        #     visited.add(cur)
        #     cur=cur.next
        #
        # return False

        # Two Pointer T=O(n) S=O(1)
        fast=slow=head

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast == slow:# the two pointers will finally meet if there is a cycle in the linked list
                return True

        return False



if __name__ == '__main__':
    solution=Solution()
    print(solution.hasCycle())