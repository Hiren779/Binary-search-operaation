class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self,data):
        
        if data == self.data:
            return
        if data < self.data:
            
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
                
    def in_order_traversal(self):
        
        elements = []
       
        if self.left:
           
            elements += self.left.in_order_traversal()
           
        elements.append(self.data) 
        
        if self.right:
            elements += self.right.in_order_traversal()
          
        return elements
    
    
    def pre_order_traversal(self):
        
        elements = []

        elements.append(self.data) 
        
        if self.left:
            elements += self.left.pre_order_traversal()
#             print("element left",elements)
     
        if self.right:
            elements += self.right.pre_order_traversal()
#             print("element right",elements)

        # add right node
        return elements
    
    def post_order_traversal(self):
        
        elements = []

        
        if self.left:
            elements += self.left.post_order_traversal()

     
        if self.right:
            elements += self.right.post_order_traversal()

            
        elements.append(self.data) 

        return elements
    
    
    
    def search(self, val):
        if self.data == val:
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
    def minimum(self):
        minim = self.data
    
        if self.left:
            minim = self.left.minimum()
        else:
            pass
 
        return minim

    def maximum(self):
        maxim = self.data
        if self.right:
            maxim = self.right.minimum()
        else:
            pass
 
        return maxim
    
    def summation(self):
        sum_of_elements = self.data
        if self.left:
            sum_of_elements += self.left.summation()
        if self.right:
            sum_of_elements += self.right.summation()
        return sum_of_elements
            

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    
    numbers_tree = build_tree([30,20,15,18,25,5,40,35,50,45,60])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    print("pre order traversal gives this sorted list:",numbers_tree.pre_order_traversal())
    print("post order traversal gives this sorted list:",numbers_tree.post_order_traversal())
    print(numbers_tree.search(20))
    print(numbers_tree.minimum())
    print(numbers_tree.maximum())
    print(numbers_tree.summation())
    
