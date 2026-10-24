class DoublyLinkedList:
    def __init__(self, key=0, val=0):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.dict={}# key->DoublyLinkedList
        self.head=DoublyLinkedList(-1,-1)
        self.tail=DoublyLinkedList(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head

    def add(self, node: DoublyLinkedList)->None:
        realTail=self.tail.prev
        realTail.next=node
        node.prev=realTail
        self.tail.prev=node
        node.next=self.tail

    def remove(self, node: DoublyLinkedList)->None:
        node.prev.next=node.next
        node.next.prev=node.prev

    def get(self, key: int)->int:
        if key not in self.dict:
            return -1
        node=self.dict[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, val: int)->None:
        # 若存在，则先删除老节点
        if key in self.dict:
            nodeToPush=self.dict[key]
            self.remove(nodeToPush)

        # 加入新节点
        node=DoublyLinkedList(key,val)
        self.add(node)
        self.dict[key]=node

        # 检查capacity是否超出
        if len(self.dict)>self.capacity:
            nodeToDelete=self.head.next
            self.remove(nodeToDelete)
            del self.dict[nodeToDelete.key]