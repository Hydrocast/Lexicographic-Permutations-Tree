from abc import ABC, abstractmethod
from queue import Empty

class Tree(ABC):
    """Abstract base class representing a tree structure."""

    @abstractmethod
    def root(self):
        """Return the root of the tree (or None if tree is empty)."""
        pass

    @abstractmethod
    def parent(self, p):
        """Return the parent of node p (or None if p is root)."""
        pass

    @abstractmethod
    def children(self, p):
        """Return an iterable of children of node p."""
        pass

    @abstractmethod
    def num_children(self, p):
        """Return the number of children of node p."""
        pass

    @abstractmethod
    def is_empty(self):
        """Return True if the tree is empty."""
        pass
    @abstractmethod
    def breadth_first_traversal(self):
        
        pass
    
    @abstractmethod
    def construction_helper(self):
        
        pass
    
    @abstractmethod
    def construct_tree(self):
        
        pass
    
    @abstractmethod
    def print_ancestry_helper(self):
        
        pass
    
    @abstractmethod
    def create_permutations(self):
        
        pass    


class LinkedTree(Tree):
    """Concrete class implementing a linked structure tree."""
    class Node:
        """Nested Node class to store tree elements."""
        def __init__(self, element, parent=None):
            self.element = element
            self.parent = parent
            self.children = []

    def __init__(self):
        """Create an initially empty tree."""
        self._root = None
        self._size = 0
    
    def root(self):
        """Return the root of the tree."""
        return self._root

    def parent(self, p):
        """Return the parent of node p."""
        return p.parent

    def children(self, p):
        """Return an iterable of the children of node p."""
        return p.children

    def num_children(self, p):
        """Return the number of children of node p."""
        return len(p.children)

    def is_empty(self):
        """Return True if the tree is empty."""
        return self._size == 0

    def add_root(self, element):
        """Place element at the root of the tree and return the new node."""
        if self._root is not None:
            raise ValueError('Root exists')
        self._root = self.Node(element)
        self._size = 1
        return self._root

    def add_child(self, p, element):
        """Create a new child for node p with element and return the new node."""
        new_node = self.Node(element, p)
        p.children.append(new_node)
        self._size += 1
        return new_node
    
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size
    
    def breadth_first_traversal(self,root):
        temp = []
        temp.append(root)
        while temp:
            new_node = temp.pop(0)
            for child in new_node.children:
                temp.append(child)
                
    def construction_helper(self,node):
        cn = 0
        for child in node.parent.children:
            cn += 1
        if cn <= 2:
            return
        for sibling in node.parent.children:
            if sibling.element != node.element:
                self.add_child(node,sibling.element)
        for child in node.children:
            self.construction_helper(child)
    
    def construct_tree(self,n):
        self.add_root(1)
        if n > 1:
            for i in range(2,n+1):
                self.add_child(self._root,i)
            for child in self._root.children:
                self.construction_helper(child)
    
    def print_ancestry_helper(self, node, temp2):
        if node is not None:
            temp2.append(node)
            return self.print_ancestry_helper(node.parent, temp2)
        else:
            parent = temp2[0].parent
            sibling = [child for child in parent.children if child != temp2[0]][0]
            return sibling

    def create_permutations(self, root):
        temp = [root]
        print()
        while temp:
            new_node = temp.pop(0)
            if not new_node.children:
                temp2 = []
                temp3 = self.print_ancestry_helper(new_node,temp2)
                temp2 = [temp3] + temp2
                print("{", end=" ")
                for i in range(len(temp2) - 1, -1, -1):
                    print(temp2[i].element, end=", " if i > 0 else " ")
                print("}")
            for child in new_node.children:
                temp.append(child)
                
    def mixer(self):
        for i in range (2,n+1):
            self.breadth_first_traversal(self._root)
            temp = []
            temp.append(self._root)
            while temp:
                new_node = temp.pop(0)
                if new_node.element == i:
                    new_node.element = self._root.element 
                for child in new_node.children:
                    temp.append(child)
            self._root.element = i
            self.create_permutations(self._root)

if __name__ == '__main__':
    tree = LinkedTree()
    
    # Loop until a valid positive integer is entered
    while True:
        try:
            n = int(input("Enter a positive integer n: "))
            if n <= 0:
                raise ValueError("Number must be positive.")
            break
        except ValueError as ve:
            print(f"Invalid input: {ve}. Please try again.\n")
    
    # Construct the tree
    print(f"\nConstructing permutation tree for n = {n}...\n")
    tree.construct_tree(n)
    
    # Initial permutations from the basic tree
    print("Initial permutations:")
    print("-" * 30)
    tree.breadth_first_traversal(tree._root)
    tree.create_permutations(tree._root)
    
    # Generate all permutations with root swapping
    print("\nGenerating all lexicographic permutations:")
    print("-" * 40)
    tree.mixer()
    
    print("\nAll permutations have been generated successfully!")
