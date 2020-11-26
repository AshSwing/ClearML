from ..base import Datastructure

class BinaryTree(Datastructure):
    """二叉树
    """
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    @property
    def is_leaf(self):
        return True if self.depth == 1 else False

    def __len__(self):
        stack = [self]
        count = 0
        while stack:
            node = stack.pop()
            count += 1
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return count

    def __repr__(self):
        string = f"<ClearML Data Structure - BinaryTree Depth({self.depth}) Value({self.value})>"
        return string

    @property
    def depth(self):
        stack = [(1, self)]
        max_depth = 0
        while stack:
            depth, node = stack.pop()
            max_depth = max(depth, max_depth)
            if node.left is not None:
                stack.append((depth+1, node.left))
            if node.right is not None:
                stack.append((depth+1, node.right))
        return max_depth

    @property
    def is_balance(self):
        if self.is_leaf:
            return True
        if self.left is None and self.right.depth == 1:
            return True
        elif self.right is None and self.left.depth == 1:
            return True
        elif self.left.is_balance and self.right.is_balance and abs(self.left.depth-self.right.depth)<=1:
            return True
        else:
            return False

    def layer(self, n):
        """二叉树横切面
        获取二叉树深度n的横切面节点数组, 超过深度范围的n会自动调整
        """
        n = n if n < self.depth else self.depth
        n = n if n > 0 else 1
        layer_list = []
        for index in range(2**(n-1), 2**n):
            bit = index
            path = []
            while bit != 1:
                path.append(bit % 2)
                bit //= 2
            path.reverse()
            cursor = self
            for p in path:
                if cursor.is_leaf:
                    cursor = None
                    break
                elif p == 0 and cursor.left is None:
                    cursor = None
                    break
                elif p == 1 and cursor.right is None:
                    cursor = None
                    break
                else:
                    cursor = cursor.right if p else cursor.left
            layer_list.append(cursor)
        return layer_list

    #XXX: 绘制二叉树符号图像
    def draw(self):
        for depth in range(self.depth):
            layer = list(map(lambda x: str(x.value) if x is not None else '*', self.layer(depth+1)))
            print(layer)