class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        
    def getNode(self,index):
        dummy = self.head
        ind = 0
        while ind < index and dummy :
            ind += 1
            dummy = dummy.next
        if dummy:
            return dummy
        return None

    def get(self, index: int) -> int:
        node = self.getNode(index)
        if node: return node.val
        return -1


    def addAtHead(self, val: int) -> None:
        dummy = Node(val)
        dummy.next = self.head
        self.head = dummy
        

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        dummy = self.head
        if dummy == None:
            self.head = node
            return

        while dummy.next:
            dummy = dummy.next

        dummy.next = node
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            return self.addAtHead(val)

        startNode = self.getNode(index-1)
        node = Node(val)
        if startNode:
            node.next = startNode.next
            startNode.next = node

    def deleteAtIndex(self, index: int) -> None:
        if index == 0 and self.head:
            self.head = self.head.next
            return 
        startNode = self.getNode(index-1)
        if startNode and startNode.next:
            startNode.next = startNode.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)