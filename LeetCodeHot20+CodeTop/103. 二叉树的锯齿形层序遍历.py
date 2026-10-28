from typing import List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

def zigzagLevelOrder(root: TreeNode)->List[List[int]]:
    # Edge Case
    if not root:
        return []

    result=[]# 记录最后zigzag结果
    queue=deque()# 储存层序遍历每层要遍历的节点
    queue.append(root)
    direction=True# 记录zigzag方向，True为左向右

    while queue:
        level=[]# 记录当前层的zigzag遍历结果
        size=len(queue)# 记录当前层要遍历多少节点
        # 遍历当前层
        for i in range(size):
            node=queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        # 每层翻转
        if not direction:
            level.reverse()
        direction=not direction

        result.append(level)

    return result