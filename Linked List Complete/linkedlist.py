from node import Node

class LinkedList:
    def __init__(self, value=None):
        self.head = Node(value)
        
    def get_current_head(self):
        return self.head

    def add_to_list(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.head)
        self.head = new_node

    def stringify(self):
        stringified = ''
        current_node = self.get_current_head()
        while current_node:
            if current_node.get_value() != None:
                stringified += current_node.get_value() + '\n'
            current_node = current_node.get_next_node()
        return stringified

    def delete_from_list(self, value):
        current_node = self.get_current_head()
        if current_node.get_value() == value:
            self.head = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node