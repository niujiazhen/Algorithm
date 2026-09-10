class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

# 反转从head开始的前K个链表节点
def reverseLinkedList(head: ListNode, k: int)->ListNode:
    prev=None
    cur=head

    while k:
        temp=cur.next# 记录cur.next
        cur.next=prev# 反转
        prev=cur# prev指向cur
        cur=temp# 遍历下一个
        k-=1

    # 返回反转后的新的头节点
    return prev

def reverseKGroup(head: ListNode, k: int)->ListNode:
    cnt=0
    cur=head

    # 首先判断当前head节点开始，是否还有K个节点
    while cur and cnt<k:
        cnt+=1
        cur=cur.next

    # 如果有k个节点，则开始反转
    if cnt==k:
        # 从head开始反转前k个节点，返回反转后的链表头
        reversedHead=reverseLinkedList(head,k)

        # 注意现在head已经是反转后的尾节点了
        # 开始递归处理后续链表，让head接上下k个反转后的链表节点头
        head.next=reverseKGroup(cur,k)

        # 返回反转的新链表头节点
        return reversedHead
    # 如果没有k个节点，则不反转，直接返回head节点
    return head