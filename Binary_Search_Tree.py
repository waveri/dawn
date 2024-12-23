class BinarySearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements=[]

        if self.left:
            elements+=self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements+=self.right.in_order_traversal()

        return elements

    def search(self,val):
        if val == self.data:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.in_order_traversal()

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        if self.right:
            elements += self.right.in_order_traversal()

        elements.append(self.data)

        return elements

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def find_min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()

    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left=self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right=self.right.delete(val)
        else:   #when val==self.data(node to be deleted found)
            if self.left is None and self.right is None:    #when no children
                return None
            elif self.left is None:     #when right child available only
                return self.right
            elif self.right is None:    #when left child available only
                return self.left

            #when two children available,pick min valued element from right subtree to replace current node
            min_val=self.right.find_min()
            self.data=min_val
            self.right=self.right.delete(min_val)

        return self

    def delete_exer(self,val):
        if val < self.data:
            if self.left:
                self.left=self.left.delete_exer(val)
        elif val > self.data:
            if self.right:
                self.right:self.right.delete_exer(val)
        else:   #when val==self.data(node to be deleted found)
            if self.left is None and self.right is None:    #when no children
                return None
            elif self.left is None:     #when right child available only
                return self.right
            elif self.right is None:    #when left child available only
                return self.left

            #when two children available,pick max valued element from left subtree to replace current node
            max_val=self.left.find_max()
            self.data=max_val
            self.left=self.left.delete_exer(max_val)

        return self

def build_tree(elements):
    root=BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__=='__main__':
    numbers=[5,2,3,98,6,54,23,12,78,55]
    numbers_tree=build_tree(numbers)
    print(numbers_tree.pre_order_traversal())