class Node:
    def __init__ (self, data):
        self.left = None
        self.data = data
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self. i = -1
        self.newnode = None
        
    def Buildtree(self,nodes):
        self.i = self.i + 1
        print(nodes[self.i])
        if (nodes[self.i] == -1):
            return None
        else:
            self.newnode = Node(nodes[self.i])
            self.newnode.left = self.Buildtree(nodes)
            self.newnode.right = self.Buildtree(nodes)
        
        return self.newnode 
            
t = BinaryTree()
root = t.Buildtree([1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]),
print(root.data)