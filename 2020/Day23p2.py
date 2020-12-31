class Node: 

    def __init__(self, label): 
        self.label = label
        self.prev = None
        self.next = None

class CircularLinkedList: 

    def __init__(self):  
        self.lookup = {}

    def push(self, label, prev_label, next_label):
        node = Node(label)
        self.lookup[label] = node
        if prev_label:
            prev_node = self.lookup[prev_label]
            prev_node.next = node
            node.prev = prev_node
        next_node = self.lookup[next_label]
        next_node.prev = node
        node.next = next_node

    def getNextLabel(self, label):
        return self.lookup[label].next.label

    def removeNode(self, label):
        node = self.lookup[label]
        node.next.prev = node.prev
        node.prev.next = node.next
        del self.lookup[label]

    def cupExists(self, label):
        return label in self.lookup

def move(cups, curr_label):

    # Get three cups after current cup and remove from list
    three_cups = []
    for _ in range(3):
        next_label = cups.getNextLabel(curr_label)
        three_cups.append(next_label)
        cups.removeNode(next_label)

    # Find destination cup
    dest_label = curr_label - 1
    while not cups.cupExists(dest_label):
        dest_label = dest_label - 1
        if dest_label < 1:
            dest_label = n_cups

    # Place three cups after destination cup
    for cup_label in three_cups:
        cups.push(cup_label, dest_label, cups.getNextLabel(dest_label))
        dest_label = cup_label

    # Return new current cup
    return cups.getNextLabel(curr_label)

if __name__ == '__main__':
    
    inp = '193467258'
    n_cups = int(1e6)
    n_moves = int(1e7)

    cups = CircularLinkedList()
    first_label = int(inp[0])
    prev_label = None

    for c in inp:
        label = int(c)
        cups.push(label, prev_label, first_label)
        prev_label = label

    for label in range(10, n_cups+1):
        cups.push(label, prev_label, first_label)
        prev_label = label

    curr_label = first_label
    for _ in range(n_moves):
        curr_label = move(cups, curr_label)

    c1 = cups.getNextLabel(1)
    c2 = cups.getNextLabel(c1)

    print(c1*c2)