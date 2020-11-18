"""
学到三点：
1. node 增删改放在cache类里面更合理；
2. 删除最后一个节点时候，忘了把repo里面的key也pop掉；
3，为啥node也要存key呢，因为删除最后一个节点需要删除key，如果不存key，
   需要挨个去查找key，复杂度变成O(n)
4. 移动到头结点，我给忘了删除原来节点位置了；
5. 增加头结点，先让原来第1个节点pre指向新的node，再让head next指向new——node；
   不然第一个节点被new_node代替了

"""
class DLinkNode(object):
    def __init__(self, key=0 , value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None



class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.repo = dict()
        self.head = DLinkNode()
        self.tail = DLinkNode()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.capacity = capacity
        self.size = 0


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.repo:
            self.move_to_head(self.repo[key])
            return self.repo[key].value
        return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.repo:
            node = self.repo[key]
            node.value = value
            self.move_to_head(node)

        else:
            new_node = DLinkNode(key, value)
            self.repo[key] = new_node
            self.add_to_head(new_node)
            self.size += 1
            if self.size > self.capacity:
                removed_node = self.tail.pre
                self.repo.pop(removed_node.key)
                self.remove_node(removed_node)
                self.size -= 1


    def add_to_head(self, node):
        head = self.head
        node.pre = head
        node.next = head.next
        head.next.pre = node
        head.next = node

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)

    def remove_node(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        node.next = node.pre = None


if __name__ == "__main__":
    c = LRUCache(2)
    c.put(1,1)
    c.put(2,2)
    c.get(1)
    c.put(3,3)
    c.get(2)
    c.put(4,4)
    c.get(1)
    c.get(3)
    c.get(4)




