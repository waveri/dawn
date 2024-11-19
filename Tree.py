class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent

        return level

    def print_tree(self):
        spaces=' '*self.get_level()*3
        prefix=spaces+'|__' if self.parent else'->'
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root=TreeNode("Cleats")

    nike=TreeNode("Nike")
    nike.add_child(TreeNode("Mercurial"))
    nike.add_child(TreeNode("Magista"))
    nike.add_child(TreeNode("Phantom"))

    adidas=TreeNode("Adidas")
    adidas.add_child(TreeNode("Ghosted"))
    adidas.add_child(TreeNode("Nemesiz"))
    adidas.add_child(TreeNode("Copa"))

    puma=TreeNode("Puma")
    puma.add_child(TreeNode("King"))
    puma.add_child(TreeNode("Future"))
    puma.add_child(TreeNode("One"))

    root.add_child(nike)
    root.add_child(adidas)
    root.add_child(puma)

    return root

if __name__=='__main__':
    root=build_product_tree()
    root.print_tree()
    pass