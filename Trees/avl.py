from bst import TreeNode, BST


class TreeNode(TreeNode):
    def __init__(self, value):
        assert value != None, "You can't use None as a value!!"
        self.data = value
        self.parent = None
        self.left = None
        self.right = None

    def set_left(self, new_node):
        self.left = new_node
        self.left.parent = self

    def set_right(self, new_node):
        self.right = new_node
        self.right.parent = self


class AVL(BST):
    def __init__(self, value):
        self.root = TreeNode(value)

    def __get_depth(self, start_node):
        depth = 0
        if start_node != None:
            left_depth, right_depth = 0, 0
            if start_node.left:
                left_depth = 1 + self.__get_depth(start_node.left)
            if start_node.right:
                right_depth = 1 + self.__get_depth(start_node.right)
            depth += max(left_depth, right_depth)
        return depth

    def __is_balanced(self, start_node):
        """
        Tree is said to be balanced if the difference between the depth of any
        two leaf nodes is one or less.
        """
        # check left subtree
        left_depth = 1 if start_node.left != None else 0
        left_depth += self.__get_depth(start_node.left)
        # check right subtree
        right_depth = 1 if start_node.right != None else 0
        right_depth += self.__get_depth(start_node.right)
        return abs(left_depth - right_depth) <= 1

    def rotate_left(self, start_node):
        middle = start_node.right
        middle.parent = start_node.parent
        middle.set_left(start_node)
        start_node.right = None
        return middle








if __name__ == "__main__":
    # to test left rotation
    avl = AVL(1)
    avl.root.set_right(TreeNode(2))
    avl.root.right.set_right(TreeNode(3))
    avl.root.right.right.set_right(TreeNode(4))
    avl.root.right.right.right.set_right(TreeNode(5))
    avl.root = avl.rotate_left(avl.root)
    avl.root.right = avl.rotate_left(avl.root.right)
    print(avl)

    