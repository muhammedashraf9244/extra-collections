class TreeNode():
    def __init__(self, value):
        # assert value != None, "You can't use None as a value!!"
        self.data = value
        self.left = None
        self.right = None
        # self.level = None

    def __repr__(self):
        return str(self.data)



class BinaryTree():
    def __init__(self, value):
        self.root = TreeNode(value)

    def __get_height(self, start_node):
        height = 0
        if start_node != None:
            left_height, right_height = 0, 0
            if start_node.left:
                left_height = 1 + self.__get_height(start_node.left)
            if start_node.right:
                right_height = 1 + self.__get_height(start_node.right)
            height += max(left_height, right_height)
            # print(start_node.data, left_height, right_height)
        return height


    def get_height(self):
        return self.__get_height(self.root)


    def __print_subtree(self, start_node):
        # get children
        left_nodes = self.__get_num_children(start_node.left)
        right_nodes = self.__get_num_children(start_node.right)
        line1 = '-'*left_nodes + str(start_node.data) + '-'*right_nodes
        line2 = '|'+(' '*(len(line1)-1))+'|'
        line3 = self.__print_subtree()
        return " {} \n {} ".format(line1, line2)


    def __get_num_children(self, start_node):
        total_nodes = 0
        if start_node != None:
            total_nodes += 1
            if start_node.left:
                total_nodes += self.__get_num_children(start_node.left)
            if start_node.right:
                total_nodes += self.__get_num_children(start_node.right)
        return total_nodes


    def __repr__(self):
        return self.__print_subtree(self.root)


    def __len__(self):
        return self.__get_num_children(self.root)






if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    tree.root.left.left = TreeNode(4)
    # tree.root.left.right = TreeNode(5)
    tree.root.left.left.right = TreeNode(100)
    #################################
    print("Tree Nodes:", len(tree))
    print("Tree Height:", tree.get_height())
    # print(tree)
    # print(tree.root, tree.root.left.right, tree.root.left.left)