from typing import Optional


class Node:

    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class Tree:

    def __init__(self):
        self.root = None


    def __find(self, node, parent, value):  # корень дерева, родительская вершина от корня (всегда None), данные которые записаны в объекте

        if node is None:
            return None, parent, False

        if value == node.val:
            return node, parent, True

        if value < node.val:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.val:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.val)

        if not fl_find and s:
            if obj.val < s.val:
                s.left = obj
            else:
                s.right = obj

        return obj

    def show_tree(self, node):
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)

    # def del_node(self, key):  # https://www.youtube.com/watch?v=mdkwm5FUpFs

    def same_tree(self, p: Optional[Node], q: Optional[Node]) -> bool:
        """ leetcode 100 problem"""

        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.same_tree(p.left, q.left) and self.same_tree(p.right, q.right)

    def get_max_deep_tree(self, root: Optional[Node]) -> int:
        """ Leetcode 104. Maximum Depth of Binary Tree """

        if root is None:
            return 0

        left_deep = self.get_max_deep_tree(root.left)
        right_deep = self.get_max_deep_tree(root.left)

        return max(left_deep, right_deep) + 1


if __name__ == '__main__':
    v = [8, 10, 7, 9, 13, 16, 2, 11, 98, 27, 21, 25, 77, 20, 98, 1, 3]
    t = Tree()
    for x in v:
        t.append(Node(x))

    print(t.get_max_deep_tree(t.root))




