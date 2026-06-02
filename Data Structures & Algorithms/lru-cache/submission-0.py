class Node:
    def __init__(self,key:int,val:int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hash = {} # key , ptr

        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next,self.right.prev = self.right,self.left
        
    def insert(self,node:Node):
        right_node = self.right.prev
        right_node.next = node
        node.prev= right_node
        node.next = self.right
        self.right.prev = node

    def remove(self,node:Node):
        prev,next = node.prev,node.next 
        prev.next = next
        next.prev = prev


    def get(self, key: int) -> int:
        if key in self.hash:
            self.remove(self.hash[key])
            self.insert(self.hash[key])
            return self.hash[key].val

        return -1 
    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.remove(self.hash[key])
        self.hash[key] = Node(key,value)
        self.insert(self.hash[key])

        if len(self.hash) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.hash[lru.key]
        
