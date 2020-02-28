from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #thought - this strategy does not account for if the value is in the ring buffer
        #since you have to traverse the whole ring to know if it is in there (no cache)
        #so likely not the most efficient implementation or a downside of using a ring buffer

        
        #if we have not met capacity...
            #Add the item
            #update where newest entry is located
        #if the ring is at capacity:
            #add new item at location of oldest item
            #update where newest entry is located
        
        #if not at capacity
        if len(self.storage) < self.capacity:
            #add the new value to the tail.
            #using the .add_to_tail method of the DLL class
            self.storage.add_to_tail(item)
            #set the current value in the Ring Buffer class to the tail.
            #this determines the entry point for new values
            self.current = self.storage.tail
        

        if len(self.storage) == self.capacity:
            #since the current value of the Ring Buffer class is set
            # to be the tail of the DLL
            #(see previous if statement above)
            # and we are at capacity
            # set the tail's new value to be the new item!
            self.current.value = item

            #Now we update each value by one down the DLL.
            #we use the is operator instead of ==
            #because we are not checking if the values are the same
            #we are checking if they are referencing the same ID in memory
            
            #if the current value is the tail of the DLL...
            #in other words, we got to the end of our ring buffer
            if self.current is self.storage.tail:
                #we set the current value to be the head of the DLL
                #so we can cycle through all the values in the list all over again.
                #This creates a circular chain of nodes... like a ring!
                self.current = self.storage.head
            else:
                #in the event the current value is not the tail of the DLL
                #we shift to the next value in the DLL - the now oldest entry.
                self.current = self.current.next

            #with the new value set, we need to update the order of the list so that this
            #current object with the updated value is set to the tail.
        


        

    def get(self):
        # Note:  This is the only [] allowed
        # ALSO - no None values should be returned
        list_buffer_contents = []

        #start at oldest value in the list
        
        list_item = self.storage.head

        while list_item:
            #cycle through values in the ring buffer
            #by going until there is no more 'next' value

            #but skip if a given item in the list is None
            if list_item.value == None:
                list_item = list_item.next
            else:
                list_buffer_contents.append(list_item.value)
                #eventually the end of the list will
                #not have a .next pointer, breaking the while loop
                list_item = list_item.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
