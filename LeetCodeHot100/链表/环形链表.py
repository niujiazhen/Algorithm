from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        set1=set()
        dummy_head=ListNode(0)
        dummy_head.next=head
        cur=dummy_head
        while(cur.next):
            if(cur.next in set1):
                return True
            set1.add(cur.next)
            cur=cur.next
        return False




if __name__ == '__main__':
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node1
    solution=Solution()
    print(solution.hasCycle(node1))
