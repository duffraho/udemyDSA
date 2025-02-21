class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        temp = self.head
        pre = temp
        if self.head is None:
            print(None)
        elif self.head.next is None:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            while temp.next is not None:
                pre = temp
                temp = temp.next
            pre.next = None
            self.tail = pre
            self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            temp = self.head
            self.head = None
            self.tail = None
            self.length = 0
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
        return temp
    
    ''' minha tentativa de fazer o get (até que funcionou)
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        ind = 0
        while temp:
            if ind == index:
                return temp.value
            else:
                temp = temp.next
                ind += 1
    '''

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        # underline no loop qdo eu só preciso iterar N vzs
        # usar i qdo eu precisar usar o valor de i
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value
        return temp
    
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        

my_LinkedList = LinkedList(0)
my_LinkedList.append(1)
my_LinkedList.append(2)
my_LinkedList.append(3)
print(my_LinkedList.get(3))