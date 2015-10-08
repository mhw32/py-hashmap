# Code adapted from: https://gist.github.com/bshyong/8205644

# Node class in the binary search tree. Each node stores the size of its own subtree, its parent, and a key to identify it.
class Node(object):
    def __init__(self, parent, idx, value):
        self.key = idx
        self.value = value
        self.size = 1 
        self.parent = parent
        self.left = None
        self.right = None
    
    # Update the size (important!)
    def update(self):
        self.size = (0 if self.left is None else self.left.size) + (0 if self.right is None else self.right.size) 

    # Add an additional member to the Node.
    def insert(self, idx, value):
        self.size += 1
        if idx < self.key:
            if self.left is None:
                self.left = Node(self, idx, value)                
                return self.left
            else:
                return self.left.insert(idx, value)
        else:
            if self.right is None:
                self.right = Node(self, idx, value)   
                return self.right
            else:
                return self.right.insert(idx, value)

    # Search the Node for a member.
    def search(self, idx):
        if idx == self.key:
            return self
        elif idx < self.key:
            if self.left is None:
                return None
            else:
                return self.left.search(idx)
        else:
            if self.right is None:
                return None
            else:
                return self.right.search(idx)

    # Returns Node with the smallest key in the subtree.
    def minimum(self): # Basically walks down the tree.
        current = self
        while current.left is not None:
            current = current.left
        return current
        
    # Returns the node with the smallest key larger than this node's key, or None if this has the largest key in the tree.
    def successor(self):
        if self.right is not None:
            return self.right.minimum()
        current = self
        while current.parent is not None and current.parent.right is current:
            current = current.parent
        return current.parent

    # Delete the Node from tree
    def delete(self):
        # Basically to delete, set the pointer of the parent directly onto the subtree. No need to handle garbage collecvtion.
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent 
            current = self.parent
            while current.key is not None:
                current.update()
                current = current.parent
            return self
        else:
            s = self.successor()
            self.key, s.key = s.key, self.key
            return s.delete()        
            
    def __repr__(self):
        return "<Node, key:" + str(self.key) + ">"

# Binary search tree implementation. Each tree contains some (possibly 0) Node objects, representing nodes and a pointer to the root.
class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.psroot = self.Node(None, None)
    
    def reroot(self):
        self.root = self.psroot.left

    # Insert into the tree.
    def insert(self, idx, value):
        if self.root is None:
            self.psroot.left = self.Node(self.psroot, idx, value)
            self.reroot()
            return self.root
        else:
            return self.root.insert(idx)
    
    # Return the node for key t if is in the tree. Default None.
    def search(self, idx):
        if self.root is None:
            return None
        else:
            return self.root.search(idx) 
    
    # Delete the node for key t if it is in the tree.
    def delete(self, idx):
        node = self.search(idx)
        deleted = self.root.delete()
        self.reroot()
        return deleted

    def __repr__(self):
        return "<BinarySearchTree>"
