class treenode():

    def __init__(self,value):

        self.left=None
        self.right=None
        self.value=value
        self.content=None



    def insert(self,value,content=None):
        if value<self.value:
            if self.left is None:
                self.left= treenode(value)#can be considered as an recursive function because its repeating itself
                self.left.content=content
            else:
                self.left.insert(value,content)

        else:#means when the value will be greater than the actual root value we have to move right now 
            if self.right is None:
                self.right=treenode(value)#can be considered as an recursive function because its repeating itself
                self.right.content=content
            else:
                self.right.insert(value,content)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)

        if self.right:
            self.right.inorder_traversal()



    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()

        if self.right:
            self.right.preorder_traversal()



    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()

        if self.right:
            self.right.preorder_traversal()


    def post_order(self):
        if self.left:
            self.left.post_order()

        if self.right:
            self.right.post_order()
        print(self.value)


    def find(self,value):

        if value<self.value:
            if self.left is None:
                return None

            else:
                return self.left.find(value)

        elif value>self.value:
            if self.right is None:
                return None

            else:
                return self.right.find(value)
        else:
            return self
tree=treenode(10)

tree.insert(5)
tree.insert(6)
tree.insert(7,{"data":"hello world"})
tree.insert(3)
tree.insert(1)
tree.insert(8)


# print(tree.left.right.right.right.value)

# tree.inorder_traversal()
# tree.preorder_traversal()
# tree.post_order()



print(tree.find(7).content["data"])




