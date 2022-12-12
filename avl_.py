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
    def inorder_traversal(self,values =[]):
        if self.left:
             self.left.inorder_traversal()
        values.append(self.value)

        if self.right :
            self.right.inorder_traversal()
        return values
        
    def preorder_traversal(self, values = []):
        values.append(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()
        return values


    def postorder_traversal(self, values = []):
        if self.left:
            self.left.postorder_traversal()
            
        if self.right:
            self.right.postorder_traversal()
        values.append(self.value)
        return values
                
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
def find_height(node):
    if node.left is None:
        return -1
    else:
       height_left = 1+find_height(node.left)
    if node.right is None:
        return -1
    else:
        height_right = 1+find_height(node.left)
    return max( height_left,height_right)
def is_balanced(node):
    if node.left is None:
        return -1
    else:
       height_left = 1+find_height(node.left)
    if node.right is None:
        return -1
    else:
        height_right = 1+find_height(node.left)
    if abs(height_left-height_right)<=1:
        return True
    else:
        return False
    


        
        
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
print(find_height(tree))
print(is_balanced(tree))

print(tree.inorder_traversal())

print(tree.postorder_traversal())

print(tree.preorder_traversal())

print(tree.find(12).content)
    
