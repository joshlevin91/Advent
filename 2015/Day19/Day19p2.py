import re

class Node(object):
    def __init__(self, data):
        self.data = data
        self.parent = self
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)
        obj.parent = self

    def make_replacements(self, replacements, med_molecule):
        molecule_found = False

        for replacement in replacements:
            matches = re.finditer(replacement[0], self.data)
            match_positions = [match.start() for match in matches]

            for pos in match_positions:
                new_molecule_data = self.data[:pos] + replacement[1] + self.data[pos+len(replacement[0]):len(self.data)]
                #print("New molecule:", new_molecule_data)
                self.add_child(Node(new_molecule_data))

                if new_molecule_data == med_molecule:
                #if new_molecule_data == "CRnSiAlYFYFArF":
                    molecule_found = True

        return molecule_found

    def sibling_exists(self):
        if self.parent == self:
            return False, None
        else:
            i = self.parent.children.index(self) + 1
            if i < len(self.parent.children):
                return True, i
            else:
                return False, None

    def get_next_child(self):
        if self.parent == self:
            return self.children[0]
        i = 0
        while True:
            if len(self.parent.children[i].children) == 0:
                i += 1
            else:
                break
        return self.parent.children[i].children[0]


    def get_next_node(self):
        has_sib, i_sib = self.sibling_exists()
        #print("Has sibling:", has_sib, "Sibling index:", i_sib)
        if has_sib:
            return self.parent.children[i_sib]
        else:
            return self.get_next_child()

def main():

    replacements = []
    molecule_found = False

    with open("input.txt", "r") as input_file:
        for line in input_file:
            s = line.split()
            if len(s) == 3:
                replacements.append([s[0], s[2]])
            elif len(s) == 1:
                med_molecule = s[0]

    current_node = Node('e')
    i = 0
    while not molecule_found and i < 10000:
    #for i in range(10):
        #print("\nCurrent node:", current_node.data)
        molecule_found = current_node.make_replacements(replacements, med_molecule)
        current_node = current_node.get_next_node()
        #print("Med molecule found:", molecule_found)
        i += 1
    print("\nCurrent node:", current_node.data)


main()