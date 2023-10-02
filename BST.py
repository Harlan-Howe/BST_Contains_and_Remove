from typing import Generic, TypeVar

T = TypeVar("T")


class TreeNode(Generic[T]):
    def __init__(self, value: T = None, left: "TreeNode[T]" = None, right: "TreeNode[T]" = None):
        self.value = value
        self.left = left
        self.right = right

    def has_left(self) -> bool:
        return self.left is not None

    def has_right(self) -> bool:
        return self.right is not None

    def print(self, indentation_level: int = 0) -> None:
        """
        prints out the tree in a tree-like format, in reverse in-order, so that if you turn your head, it looks like a
        normal tree.
        :param indentation_level: the number of tabs before this subtree is printed.
        :return: None
        """

        if self.has_right():
            self.right.print(indentation_level=indentation_level+1)

        print("\t"*indentation_level+self.value)

        if self.has_left():
            self.left.print(indentation_level=indentation_level+1)


class BST(Generic[T]):
    def __init__(self):
        self.root = None

    def print_tree(self):
        """
        prints out a "tree-like" arrangement of this tree. (Turn your head 90 CCW (or the laptop 90 CW) to see.)
        :return: None
        """
        if self.root is None:
            print("Empty Tree.")
        else:
            self.root.print()

    def add(self, value: T) -> bool:
        """
        Adds a new node with value in it to this tree
        :param value:  the value to add
        :return: None
        """
        if value is None:
            raise RuntimeError("Attempted to add a null value to a BST.")
        if self.root is None:
            self.root = TreeNode(value)
            return True
        else:
            return self.add_to_subtree(value, self.root)

    def add_to_subtree(self, value: T, sub_root: TreeNode[T]) -> bool:
        """
        Internal, recursive method for adding a value to a tree with a subroot in order.
        :param value: The value to add
        :param sub_root: the root of the subtree to which to add it.
        :return: Whether we successfully added a non-duplicated item.
        """
        if value < sub_root.value:
            if sub_root.has_left():
                return self.add_to_subtree(value, sub_root.left)
            else:
                sub_root.left = TreeNode(value)
                return True
        elif value > sub_root.value:
            if sub_root.has_right():
                return self.add_to_subtree(value, sub_root.right)
            else:
                sub_root.right = TreeNode(value)
                return True
        else:
            return False  # In this particular implementation, we will have no duplicates.

    def __repr__(self):
        """
        returns a string representing the words in this list, in order.
        :return: a string containing the values, in order;
        """
        if self.root is None:
            return "[]"
        return "["+self.to_string(self.root)[0:-2]+"]"

    def to_string(self, subroot: TreeNode[T]) -> str:
        result = ""
        if subroot.has_left():
            result += self.to_string(subroot.left)
        result += subroot.value + ", "
        if subroot.has_right():
            result += self.to_string(subroot.right)

        return result

    def __contains__(self, item: T) -> bool:
        """
        determines whether this item is contained in the tree already.
        :param item: the item to search for
        :return: whether the item is in this tree.
        """
        # ------------------------
        # TODO: You write this!

        # ------------------------
        return False

    def remove_item(self, item: T) -> bool:
        """
        removes the item (if contained in this BST) from the tree, leaving the tree as a BST.
        :param item: item to remove.
        :return: whether an item was removed.
        postcondition: the BST is still correctly ordered as a BST. If returning True, the size of the BST is
        reduced by one; if returning false, BST is unchanged.
        """
        if item not in self:
            return False
        # ------------------------
        # TODO: You write this!

        # first, find the node to remove and its parent.

        # once you have that node, find which node should replace it, and set up any connections. This will depend on
        #  the number of child subtrees.

        # once you have the replacement node, disconnect it from the surrounding tree, and put it in the place of the
        #   node you are removing.

        return True
