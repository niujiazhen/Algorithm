# 题目描述某操作系统采用 LRU 作为内存页面置换算法。
# 假设初始内存为空，现给定将访问的内存页序列 pages, 序列长度 page_cnt 和内存总容量(页面数) mem，请返回缺页中断的次数。
# 例如pages是[2,1, 2,3]，内存总容量mem 是 2，发生缺页中断次数是3次，因为首先 2,1进入时发生缺页，后续 2到来时 内存已有没有中断，
# 3来了发生中断，一共 3 次，此时LRU需要1淘汰，把 3放进。

# 要实现O(1)查找or删除：用双向链表
class DoublyLinkedList:
    def __init__(self,val: int, prev: None, next: None):
        self.val=val
        self.prev=prev
        self.next=next

class LRU:
    def __init__(self, mem: int):
        self.mem=mem
        self.fault=0
        self.dict=set()# hashMap实现O(1)的查询
        # 虚拟头尾节点
        self.dummyHead=DoublyLinkedList(-1)
        self.dummyTail=DoublyLinkedList(-1)
        self.dummyHead.next=self.dummyTail
        self.dummyTail.prev=self.dummyHead
        # dummyHead->      ->dummyTail

    def put(self, node:DoublyLinkedList):# 用于查询or新增节点
        # 先检验当前节点是否已经在链表里了
        if node not in self.dict:# 缺页
            # 若不在，则fault+1，然后加入set
            self.fault+=1
            self.add(node)
            self.dict.add(node)

        # 如果存在
        # 更新LRU
        self.remove(node)
        self.add(node)
        2，1，2，3   1
        # 检验长度
        if len(self.dict)>self.mem:
            # 先拿到链表头节点
            nodeToDelete=self.dummyHead.next# 要去除的头节点
            self.remove(nodeToDelete)
            self.dict.remove(nodeToDelete)





    # 辅助函数1：用于向链表里添加节点
    def add(self, node:DoublyLinkedList):
        # 找到链表尾部
        realTail=self.dummyTail.prev# 真链表尾
        # 原始尾节点和新node双向链接
        realTail.next=node
        node.prev=realTail
        # 新node和dummyTail双向链接
        self.dummyTail.prev=node
        node.next=self.dummyTail

    # 辅助函数2：用于向链表移除节点
    def remove(self,node:DoublyLinkedList):
        # 删除当前节点node
        node.prev.next=node.next
        node.next.prev=node.prev



if __name__ == '__main__':
    lru=