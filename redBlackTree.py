# Class to hold RedBlackTree Nodes
class RBNode:
    def __init__(self, ride, minHeapNode):
        self.ride = ride # ride object
        self.parent = None   # parent Node
        self.left = None  # left child
        self.right = None  #right child
        self.colour = 1  #colour of node
        self.minHeapNode = minHeapNode

#RBT Class
class RedBlackTree:
    def __init__(self):
        self.nullNode = RBNode(None, None)
        self.nullNode.left = None
        self.nullNode.right = None
        self.nullNode.colour = 0
        self.root = self.nullNode

    #search for ride in RBT based on the key value
    def getRide(self, keyVal):
        tempNode = self.root
        while tempNode != self.nullNode:
            if tempNode.ride.rNo == keyVal:
                return tempNode
            if tempNode.ride.rNo < keyVal:
                tempNode = tempNode.right
            else:
                tempNode = tempNode.left

        return None
    
    # Insert a new ride into the RBT
    def insert(self, ride, min_heap):
        node = RBNode(ride, min_heap)
        node.parent = None
        node.left = self.nullNode
        node.right = self.nullNode
        node.colour = 1

        insertionNode = None
        tempNode = self.root

        #find the appropriate insertion point
        while tempNode != self.nullNode:
            insertionNode = tempNode
            if node.ride.rNo < tempNode.ride.rNo:
                tempNode = tempNode.left
            else:
                tempNode = tempNode.right

        #Set new nodes parent to insertion node
        node.parent = insertionNode
        if insertionNode is None:
            self.root = node
        elif node.ride.rNo > insertionNode.ride.rNo:
            insertionNode.right = node
        else:
            insertionNode.left = node
        if node.parent is None:
            node.colour = 0
            return
        if node.parent.parent is None:
            return
        self.postInsertBalance(node)

    #delete ride from the redBlackTree 
    def deleteNode(self, rNo):
        return self.deleteHelper(self.root, rNo)

    #balance the RBT after deletion
    def postDeleteBalance(self, node):
        while node != self.root and node.colour == 0:
            #rebalance tree based on wether the node is right child or left child
            if node == node.parent.right:
                parent_sibling = node.parent.left
                if parent_sibling.colour != 0:
                    node.parent.colour = 1
                    parent_sibling.colour = 0
                    self.rightRotation(node.parent)
                    parent_sibling = node.parent.left

                if parent_sibling.right.colour == 0 and parent_sibling.left.colour == 0:
                    parent_sibling.colour = 1
                    node = node.parent
                else:
                    if parent_sibling.left.colour != 1:
                        parent_sibling.right.colour = 0
                        parent_sibling.colour = 1
                        self.leftRotation(parent_sibling)
                        parent_sibling = node.parent.left

                    parent_sibling.colour = node.parent.colour
                    node.parent.colour = 0
                    parent_sibling.left.colour = 0
                    self.rightRotation(node.parent)
                    node = self.root
            else:
                parent_sibling = node.parent.right
                if parent_sibling.colour != 0:
                    node.parent.colour = 1
                    parent_sibling.colour = 0
                    self.leftRotation(node.parent)
                    parent_sibling = node.parent.right

                if parent_sibling.right.colour == 0 and parent_sibling.left.colour == 0:
                    parent_sibling.colour = 1
                    node = node.parent
                else:
                    if parent_sibling.right.colour != 1:
                        parent_sibling.left.colour = 0
                        parent_sibling.colour = 1
                        self.rightRotation(parent_sibling)
                        parent_sibling = node.parent.right
                    parent_sibling.colour = node.parent.colour
                    node.parent.colour = 0
                    parent_sibling.right.colour = 0
                    self.leftRotation(node.parent)
                    node = self.root
        node.colour = 0

    #Balance the RBT after insertion
    def postInsertBalance(self, currentNode):
        #rebalance tree while currentNode's parent is red
        while currentNode.parent.colour == 1:
            if currentNode.parent == currentNode.parent.parent.left: 
                parent_sibling = currentNode.parent.parent.right
                if parent_sibling.colour == 0:
                    if currentNode == currentNode.parent.right:
                        currentNode = currentNode.parent
                        self.leftRotation(currentNode)
                    currentNode.parent.colour = 0
                    currentNode.parent.parent.colour = 1
                    self.rightRotation(currentNode.parent.parent)
                else:
                    parent_sibling.colour = 0
                    currentNode.parent.colour = 0
                    currentNode.parent.parent.colour = 1
                    currentNode = currentNode.parent.parent
            else:
                parent_sibling = currentNode.parent.parent.left
                if parent_sibling.colour == 0:
                    if currentNode == currentNode.parent.left:
                        currentNode = currentNode.parent
                        self.rightRotation(currentNode)
                    currentNode.parent.colour = 0
                    currentNode.parent.parent.colour = 1
                    self.leftRotation(currentNode.parent.parent)
                else:
                    parent_sibling.colour = 0
                    currentNode.parent.colour = 0
                    currentNode.parent.parent.colour = 1
                    currentNode = currentNode.parent.parent
            if currentNode == self.root:
                break
        self.root.colour = 0

#Helper functions for RBT operations:
    #transplant RBT
    def rbTransplant(self, node, child_node):
        if node.parent is None:
            self.root = child_node
        elif node == node.parent.right:
            node.parent.right = child_node
        else:
            node.parent.left = child_node
        child_node.parent = node.parent

    #helper for deletion
    def deleteHelper(self, node, keyVal):
        deleteNode = self.nullNode
        while node != self.nullNode:
            if node.ride.rNo == keyVal:
                deleteNode = node
            if node.ride.rNo >= keyVal:
                node = node.left
            else:
                node = node.right
        if deleteNode == self.nullNode:
            return
        heapNode = deleteNode.minHeapNode
        y = deleteNode
        y_og_colour = y.colour
        if deleteNode.left == self.nullNode:
            x = deleteNode.right
            self.rbTransplant(deleteNode, deleteNode.right)
        elif (deleteNode.right == self.nullNode):
            x = deleteNode.left
            self.rbTransplant(deleteNode, deleteNode.left)
        else:
            y = self.minimum(deleteNode.right)
            y_og_colour = y.colour
            x = y.right
            if y.parent == deleteNode:
                x.parent = y
            else:
                self.rbTransplant(y, y.right)
                y.right = deleteNode.right
                y.right.parent = y

            self.rbTransplant(deleteNode, y)
            y.left = deleteNode.left
            y.left.parent = y
            y.colour = deleteNode.colour
        if y_og_colour == 0:
            self.postDeleteBalance(x)

        return heapNode

    #find rides wiithin a given range and append to result
    def findRideInRange(self, node, l, h, result):
        if node == self.nullNode:
            return

        if l < node.ride.rNo:
            self.findRideInRange(node.left, l, h, result)
        if l <= node.ride.rNo <= h:
            result.append(node.ride)
        self.findRideInRange(node.right, l, h, result)

    #get rides in the range
    def getRidesInRange(self, l, h):
        result = []
        self.findRideInRange(self.root, l, h, result)
        return result
    
    #find minimum node
    def minimum(self, node):
        while node.left != self.nullNode:
            node = node.left
        return node

    #left rotate RBT
    def leftRotation(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nullNode:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    #right rotate RBT
    def rightRotation(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nullNode:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

