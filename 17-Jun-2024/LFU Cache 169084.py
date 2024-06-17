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
        # print("delete :",freq, [(e[0], e[1][2]) for e in self.d_lists.items()],self.count)
        if count == 1:
            self.d_lists.pop(freq)
            self.cache.pop(key)
        else:
            if tail == node:
                new_tail = node.left
                tail = new_tail
                tail.right = None
            elif head == node:
                new_head = node.right
                head = new_head
                head.left = None
            else:
                left = node.left
                right = node.right
                left.right = right
                right.left = left
            del self.cache[key]
            self.d_lists[freq] = head,tail,count-1
        self.updatemin(freq,freq + 1)
        # print("delete :",freq, [(e[0], e[1][2]) for e in self.d_lists.items()],self.count)

    
    def add(self,key):
        self.count += 1
        _, freq, node = self.cache[key]
        # print("add <- :",freq, [(e[0], e[1][2]) for e in self.d_lists.items()],self.count)

        if freq not in self.d_lists:
            self.d_lists[freq] = node,node,1
        else:
            head,tail,count = self.d_lists[freq]
            node.right = head
            head.left = node
            self.d_lists[freq] = node, tail, count + 1
        # print("add -> :",freq, [(e[0], e[1][2]) for e in self.d_lists.items()],self.count)

    def delete_min(self):
        self.count -= 1
        mini = self.mini.key
        # print()
        # print("delete_min :", mini, [(e[0], e[1][2]) for e in self.d_lists.items()],self.count)
        # self.printm()
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
        # print("delete_min :", mini, [(e[0], e[1][2]) for e in self.d_lists.items()],self.count)
        # self.printm()
        # print()


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
        # print("get :",key, self.count)
        # self.printd(self.d_lists)
        # print("get :",(key))
        if key in self.cache:
            value,freq,_ = self.cache[key]
            self.delete(key)
            self.cache[key] = value, freq + 1, DoubleLinkedList(key)
            self.add(key)
            # print("get :",key, self.count, self.cache[key][0])
            # self.printd(self.d_lists)
            self.printm()
            return self.cache[key][0]
        return -1
        

    def put(self, key: int, value: int) -> None:
        # print("put : ",key, self.count, value)
        # self.printd(self.d_lists)
        # print("put :",(key, value))
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
        self.printm()
        # print("put : ",key, self.count,value)
        # self.printd(self.d_lists)
    def printm(self):
        return
        head = self.mini
        node = head
        l = []
        while node:
            l.append(node.key)
            node = node.right
        print(self.count,l,self.capacity)
        



        # self.counter[key] += 1
        # if key not self.cache:
        #     self.capacity += 1
        # self.cache[key] = value
        # return -1

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)