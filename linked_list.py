
class Nodes:
    def __init__(self, nodeval=None, nextval=None):
        self.nodeval = nodeval
        self.next = nextval


class linked_list:
    def __init__(self):
        self.head = Nodes()


    def insert_at_begining(self, nodeval):
       node = Nodes(nodeval, self.head)
       self.head = node

    def display(self):
        if self.head is None:
            print('Linked list is empty')
            return
        item = self.head
        itemstr = ''
        while item:
            itemstr += str(item.nodeval) + '--->'
            item = item.next
        print(itemstr)

    def insert_at_end(self, nodeval):
        if self.head is None:
            self.head = Nodes(nodeval, None)
            return
        item = self.head
        while item.next:
            item = item.next
        item.next = Nodes(nodeval, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def length(self):
        count = 0
        item = self.head
        while item:
            count += 1
            item = item.next
        return count
    def remove_at(self, index):
        if index < 0 or index >= self.length():
            raise Exception('Invalid index')
        if index == 0:
            self.head = self.head.next
        count = 0
        item = self.head
        while item:
            if count == index - 1:
                item.next = item.next.next
                break
            item = item.next
            count += 1

    def insert_at(self, index, nodeval):
        if index < 0 or index > self.length():
            raise Exception('Invalid index')
        if index == 0:
            self.insert_at_begining(nodeval)
            return

        count = 0
        item = self.head
        while item:
            if count == index - 1:
               node = Nodes(nodeval, item.next)
               item.next = node
               break
            item = item.next


my_list = linked_list()
x= []
# my_list.insert_at_begining(3)
# my_list.insert_at_begining(4)
# my_list.insert_at_begining(5)
my_list.insert_values(['banana', 'orange', 'mango', 'grapes'])

# my_list.insert_at_end(10)
# my_list.insert_at_end(6)
my_list.insert_at(3, 'figs')
# my_list.remove_at(3)
print('the length of my linked list is :', my_list.length())
my_list.display()

# print("element at 2nd index: %d" % my_list.get(2))
