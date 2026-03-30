from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def detectCycle(head: Optional[ListNode]) -> bool:
    # Edge Case
    if not head:
        return None

    # 快慢指针做法
    # T=O(n) S=O(1)
    fast=head
    slow=head

    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
        if fast == slow:
            # 如果相遇，则证明有环，然后开始找环的入口
            node1=head
            node2=fast
            while node1!=node2:
                node1=node1.next
                node2=node2.next
            return node1

    return None




if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    # node1.next = node2
    # node2.next = node3
    # node3.next = node4
    # node4.next = node1
    print(detectCycle(node1))
