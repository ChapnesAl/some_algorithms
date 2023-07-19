class Node:

    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Tree:

    def __init__(self):
        self.root = None


    def __find(self, node, parent, value):  # корень дерева, родительская вершина от корня (всегда None), данные которые записаны в объекте

        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
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



v = [8, 10, 7, 9, 13, 16, 2, 11, 98, 27 ]
t = Tree()
for x in v:
    t.append(Node(x))

