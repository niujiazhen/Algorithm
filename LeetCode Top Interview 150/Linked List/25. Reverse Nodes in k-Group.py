from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cnt=0
        cur=head

        # First check if there is enough k nodes
        while cur and cnt<k:
            cnt+=1
            cur=cur.next

        if cnt==k:
            # Reverse first k nodes
            reversedHead=self.reverseLinkeList(head,k)
            # recursion: previous head now is the tail of new k-reversed LinkeList
            head.next=self.reverseKGroup(cur,k)

            return reversedHead

        # Otherwise, just return head because we cannot reverse LinkedList anymore
        return head
    def reverseLinkeList(self,head: ListNode, k: int)->ListNode:

        prev = None
        cur = head
        # Reverse first k nodes starting from head node
        while k:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            k -= 1
        # prev is the new head of k-reversed LinkedList
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
    print(solution.reverseKGroup(node1,2))