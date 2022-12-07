class avl:
    def __init__(self,value):
        self.right = None
        self.left = None
        self.value = value
        self.content = None
    def insert(self, value, content = None):
        if value < self.value:
            if self.left is None:
                self.left = avl(value)
                self.left.content = content
            else:
                self.left.insert(value, content)
        else:
            if self.right is None:
                self.right = avl(value)
                self.right.content = content
            else:
                self.right.insert(value,content)
    def inorder_traversal(self):
        if self.left:
             self.left.inorder_traversal()
        print(self.value)

        if self.right :
            self.right.inorder_traversal()
        
    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()


    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
            
        if self.right:
            self.right.postorder_traversal()
        print(self.value)
                
    def find(self, value):
        if self.value < value:
            if self.right is None :
                return None
            else:
                return self.right.find(value)
        elif self.value> value:
            if self.left is None:
                 return None
            else:
                return self.left.find(value)
        else:
            return self
        
tree = avl(10)
tree.insert(12,{12:"Eddy"})
tree.insert(8, {8:"Olivier"})
tree.insert(11,{11:"Philbert"})
tree.insert(14)
tree.insert(9)
tree.insert(5)
tree.insert(4)
tree.insert(16)
tree.insert(13)
tree.insert(6)

tree.inorder_traversal()

print("this is postorder")
tree.postorder_traversal()
print(tree.find(12).content)
    
