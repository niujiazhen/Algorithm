# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge Case
        if not head:
            return None

        # Basic Solution
        # T=O(n) S=O(1)
        cur=head
        prev=None # previous node of cur
        while cur:
            # keep track of cur.next
            temp=cur.next
            # reverse the link
            cur.next=prev
            prev=cur
            # restore cur node to the original next node
            cur=temp

        return prev




if __name__ == '__main__':
    solution=Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print(solution.reverseList(node1))