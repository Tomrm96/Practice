from node import Node
from linkedlist import LinkedList


ll = LinkedList()

ll.add_to_list('1')
ll.add_to_list('2')
ll.add_to_list('3')
ll.add_to_list('4')
ll.add_to_list('5')


print(ll.stringify())

ll.delete_from_list('3')

print(ll.stringify())

