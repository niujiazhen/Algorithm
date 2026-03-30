from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def hasCycle(head: Optional[ListNode]) -> bool:
    # Edge Case
    if not head:
        return False

    # 快慢指针做法
    # T=O(n) S=O(1)
    fast=head
    slow=head

    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
        if fast == slow:
            return True

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
    print(hasCycle(node1))
