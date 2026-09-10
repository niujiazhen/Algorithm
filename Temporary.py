class DoublyLinkedList:
    def __init__(self, key: int, val: int):  # 用于实现O(1)增加、修改、删除节点
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}  # 用于O(1)查找节点，存储key->DoublyLinkedList，便于直接找到节点
        self.head = DoublyLinkedList(-1, -1)  # 虚拟头节点
        self.tail = DoublyLinkedList(-1, -1)  # 虚拟尾节点
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dict:  # 若不存在则返回-1
            return -1
        nodeToGet = self.dict[key]
        # 先删除再新增，从而更新LRU
        self.remove(nodeToGet)
        self.add(nodeToGet)
        # 最后返回val
        return nodeToGet.val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:  # 如果存在这个key
            nodeToModify = self.dict[key]
            self.remove(nodeToModify)
        # 新增这个节点
        newNode = DoublyLinkedList(key, value)
        self.add(newNode)
        self.dict[key] = newNode

        # 检查容量
        if len(self.dict) > self.capacity:
            nodeToDelete = self.head.next  # 需要删除的LRU节点
            self.remove(nodeToDelete)
            del self.dict[nodeToDelete.key]

    def add(self, node: DoublyLinkedList) -> None:  # 用于添加节点到链表中
        realTail = self.tail.prev  # 找到真正的尾节点
        realTail.next = node
        node.prev = realTail
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node: DoublyLinkedList) -> None:  # 用于删除节点
        node.prev.next = node.next
        node.next.prev = node.prev
