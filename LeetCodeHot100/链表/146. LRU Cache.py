class DoublyLinkedList:
    def __init__(self, key: int, val: int):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity# LRU容量
        self.dict={}# 字典实现O(1)查询, 存储key->DoublyLinkedList，便于O(1)根据key查找节点
        self.head=DoublyLinkedList(-1,-1)# 虚拟头节点，需要随时知道链表头，用于去除使用频次最低的节点
        self.tail=DoublyLinkedList(-1,-1)# 虚拟尾节点，需要随时知道链表尾，用于加入或更新节点
        self.head.next=self.tail
        self.tail.prev=self.head


    def get(self, key: int) -> int:
        # 判断不存在的情况
        if not key in self.dict:
            return -1

        # 若存在
        getNode=self.dict[key]
        self.remove(getNode)
        self.add(getNode)
        return getNode.val

    def put(self, key: int, value: int) -> None:
        # 若修改
        if key in self.dict:
            updateNode=self.dict[key]# 先删除要修改的节点
            self.remove(updateNode)

        # 若新增
        newNode=DoublyLinkedList(key,value)
        self.dict[key]=newNode
        self.add(newNode)

        #判断是否超capacity
        if len(self.dict) > self.capacity:
            deleteNode=self.head.next# 改删除的LRU节点
            self.remove(deleteNode)
            del self.dict[deleteNode.key]

    def add(self, node: DoublyLinkedList) -> None:# 向链表尾部添加新节点
        # 先找到结尾节点
        realTailNode=self.tail.prev
        # 开始加入
        realTailNode.next=node
        node.prev=realTailNode
        node.next=self.tail
        self.tail.prev=node

    def remove(self, node: DoublyLinkedList) -> None:
        node.prev.next=node.next
        node.next.prev=node.prev

if __name__ == '__main__':
    lru=LRUCache(2)
    lru.put(1,1)
    lru.put(2,2)
    lru.get(1)
    lru.put(3,3)
    lru.get(2)
    lru.put(4,4)
    lru.get(1)
    lru.get(3)
    lru.get(4)



