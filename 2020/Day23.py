
class Node: 

    def __init__(self, data): 
        self.data = data
        self.next = None
   
class CircularLinkedList: 

    def __init__(self):  
        self.head = None

    def addNodeToEnd(self, n):
        node = Node(n)
        temp = self.head

        if self.head == None:
            self.head = node
        else:
            while temp.next != self.head:
                temp = temp.next
            temp.next = node

        node.next = self.head

    def addNodeAfter(self, tail, n):
        node = Node(n)
        temp = self.head

        while temp.data != tail:
            temp = temp.next

        node.next = temp.next
        temp.next = node


    def removeNode(self, n):
        temp = self.head

        wasHead = False
        if temp.data == n:
            temp = temp.next
            wasHead = True

        while temp.data != n:
            prev = temp
            temp = temp.next

        prev.next = temp.next
        if wasHead:
            self.head = temp.next
        temp = None

    def getNextNum(self, n):
        temp = self.head
        if temp == None:
            return None
        while temp.data != n:
            temp = temp.next
        return temp.next.data

    def printList(self): 
        temp = self.head 
        while temp: 
            print(temp.data) 
            temp = temp.next
            if temp == self.head:
                break
        print('\n')

    def searchForCup(self, n):
        temp = self.head
        while temp:
            if temp.data == n:
                return temp.data
            temp = temp.next
            if temp == self.head:
                break
        return None

    def orderAfterOne(self):
        temp = self.head
        order = ''
        while temp.data != 1:
            temp = temp.next
        temp = temp.next
        while temp.data != 1:
            order += str(temp.data)
            temp = temp.next
        return order


def move(cups, curr):

    # Get three cups after current cup and remove from list
    three_cups = []
    for _ in range(3):
        num = curr
        next_num = cups.getNextNum(num)
        three_cups.append(next_num)
        cups.removeNode(next_num)
        n = next_num

    # Find destination cup
    dest = curr - 1
    while cups.searchForCup(dest) is None:
        dest = dest - 1
        if dest < 1:
            dest = 9

    # Place three cups after destination cup
    for c in three_cups:
        cups.addNodeAfter(dest, c)
        dest = c

    # Return new current cup
    return cups.getNextNum(curr)


if __name__ == '__main__':
    
    inp = '193467258'

    cups = CircularLinkedList()
    for c in inp:
        cups.addNodeToEnd(int(c))

    curr = int(inp[0])
    for _ in range(100):
        curr = move(cups, curr)

    print(cups.orderAfterOne())