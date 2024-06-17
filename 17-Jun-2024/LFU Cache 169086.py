# Problem: LFU Cache - https://leetcode.com/problems/lfu-cache/

class DoubleLinkedList:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.cache = {}
        self.d_lists = {}
        self.minis = {}
        self.mini = None

    def delete(self,key):
        self.count -= 1
        _, freq, node = self.cache[key]
        head, tail, count = self.d_lists[freq]
        if count == 1:
            self.d_lists.pop(freq)
            self.cache.pop(key)
        else:
            left = node.left
            right = node.right
            if tail == node:
                tail = left
                tail.right = None
            elif head == node:
                head = right
                head.left = None
            else:
                left.right = right
                right.left = left
            del self.cache[key]
            self.d_lists[freq] = head,tail,count-1
        self.updatemin(freq,freq + 1)

    
    def add(self,key):
        self.count += 1
        _, freq, node = self.cache[key]
        if freq not in self.d_lists:
            self.d_lists[freq] = node,node,1
        else:
            head,tail,count = self.d_lists[freq]
            node.right = head
            head.left = node
            self.d_lists[freq] = node, tail, count + 1

    def delete_min(self):
        self.count -= 1
        mini = self.mini.key
        head,tail,count = self.d_lists[mini]
        key = tail.key
        del self.cache[key]
        if count == 1:
            del self.d_lists[mini]
            self.deletemin()
        else:
            new_tail = tail.left
            new_tail.right = None
            self.d_lists[mini] = head, new_tail, count - 1

    def addmin(self):
        node = DoubleLinkedList(1)
        if self.mini == None:
            self.minis[1] = node
            self.mini = node
        elif self.mini.key != 1:
            node.right = self.mini
            self.mini = node
            self.minis[1] = node

    def deletemin(self):
        self.mini = self.mini.right

    def updatemin(self, pre, post):
        node = DoubleLinkedList(post)
        pre_node = self.minis[pre]
        if pre in self.d_lists:
            if post not in self.minis:
                node.right = pre_node.right
                pre_node.right = node
                self.minis[post] = node 
        else:
            if post not in self.minis:
                pre_node.key = post
                self.minis[post] = pre_node
            else:
                post_node = self.minis[post]
                pre_node.key = post
                pre_node.right = post_node.right
                self.minis[post] = pre_node

    def get(self, key: int) -> int:
        if key in self.cache:
            value,freq,_ = self.cache[key]
            self.delete(key)
            self.cache[key] = value, freq + 1, DoubleLinkedList(key)
            self.add(key)
            return self.cache[key][0]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.count == self.capacity:
                self.delete_min()
            self.cache[key] = value, 1, DoubleLinkedList(key)
            self.add(key)
            self.addmin()
        else:
            _,freq,_ = self.cache[key]
            self.delete(key)
            self.cache[key] = value, freq + 1, DoubleLinkedList(key)
            self.add(key)
        

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)