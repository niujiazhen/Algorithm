# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #集合set法
        hash_set=set()
        while(head):
            if(head in hash_set):
                return head
            hash_set.add(head)
            head=head.next
        return None


        #快慢指针法
        # fast=slow=head
        # while(fast and fast.next and fast.next.next):
        #     fast=fast.next.next
        #     slow=slow.next
        #     if(fast==slow):
        #         #如果相遇，则证明有环，然后开始找环的入口
        #         node1=head
        #         node2=fast
        #         while(node1!=node2):
        #             node1=node1.next
        #             node2=node2.next
        #         return node1
        # return None









if __name__ == '__main__':
    solution=Solution()
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next=node2

    print(solution.detectCycle(node1))
