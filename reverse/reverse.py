class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # TO BE COMPLETED
    #need to juggle some pointers!

    #to start, since it is a SLL
    #there is only a head, and not an established tail.
    #initializing initial values:


    #the previous value for the start of a List is None, nothing proceeds it!
    prev = None
    
    #the current node is the head of the SLL
    curr = self.head
    #while there is node to iterate through...
    while curr is not None:
      #the next node is what the current
      #node is pointing to 
      next = curr.next_node
      #what the current node is pointing to
      #is now the previous node
      curr.next_node = prev
      #with the assignment of what the next and current nodes are
      #you can reassign out dated pointers
      
      #your previous node is now what was just current
      prev = curr
      #your current node is now what is next in the list
      curr = next

      #this re-assignment is done until there are no more nodes in the list

    #for the final node, set the head of the SLL to be the final list node
    self.head = prev