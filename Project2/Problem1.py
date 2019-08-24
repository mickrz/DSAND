class Node(object):
    def __init__(self, key, value):
        self.next_ptr = None
        self.previous_ptr = None
        self.key = key
        self.value = value
    
    def get_next_ptr(self):
        return self.next_ptr
    
    def set_next_ptr(self, node):
        self.next_ptr = node
        
    def get_previous_ptr(self):
        return self.previous_ptr
    
    def set_previous_ptr(self, node):
        self.previous_ptr = node

    def get_key(self):
        return self.key
    
    def set_key(self, key):
        self.key = key
        
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value

    def __repr__(self):
        s = f"""
        Key[ {self.key}] = {self.value}
        """
        return s
    
class Linked_List(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.list_size = 0
        
    def get_head_ptr(self):
        return self.head
    
    def set_head_ptr(self, node):
        self.head = node
    
    def get_tail_ptr(self):
        return self.tail
    
    def set_tail_ptr(self, node):
        self.tail = node
        
    def prepend(self, key, value):
        self.list_size += 1
        new_node = Node(key, value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node    # add data to the next attribute of the tail (i.e. the end of the queue)
            self.tail = self.tail.next   # shift the tail (i.e., the back of the queue)
        return new_node

    def remove(self):
        self.list_size -= 1
        if self.size() < 1:
            return None
        key = self.head.key          # copy the value to a local variable
        value = self.head.value          # copy the value to a local variable
        self.head = self.head.next       # shift the head (i.e., the front of the queue)
        return (key, value)
        
    def get_oldest_key(self):
        if self.size() < 1:
            return None
        key = self.head.key          # copy the value to a local variable
        value = self.head.value          # copy the value to a local variable
        return (key, value)

    def size(self):
        return self.list_size
    
    def dump_list(self):
        while node.get_next_node_ptr():
            print(str(node))
            node = node.get_next_node_ptr()

    
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.lru_dict = dict({})
        self.lru_llist = Linked_List()
        self.cached_entries = 0

    def get_capacity(self):
        return self.capacity
    
    def get_list(self):
        return self.lru_llist
    
    def get_dictionary(self):
        return self.lru_dict
    
    def get_number_of_cached_entries(self):
        return self.cached_entries
        
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.lru_dict:
            return -1

        # remove entry from current position
        value = self.lru_dict[key].get_value()
        del self.lru_dict[key]
        self.get_list().remove()
        self.lru_dict[key] = self.get_list().prepend(key, value)
        return value
        
    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key not in self.lru_dict:
            if self.get_number_of_cached_entries() == self.get_capacity():
                lru_key, lru_value = self.get_list().get_oldest_key()
                del self.lru_dict[lru_key]
                self.cached_entries -= 1
            self.lru_dict[key] = self.get_list().prepend(key, value)
            self.cached_entries += 1
        else:
            self.lru_dict[key] = self.get_list().prepend(key, value)
            
our_cache = LRU_Cache(5)

print ("Pass" if  (-1 == our_cache.get(1)) else "Fail") # returns -1 because nothing in cache

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print ("Pass" if  (1 == our_cache.get(1)) else "Fail") # returns 1
print ("Pass" if  (2 == our_cache.get(2)) else "Fail") # returns 2
print ("Pass" if  (-1 == our_cache.get(9)) else "Fail") # returns 9

our_cache.set(5, 5) 
our_cache.set(6, 6)

print ("Pass" if  (-1 == our_cache.get(3)) else "Fail") # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

our_cache.set(6, 7)

print ("Pass" if  (7 == our_cache.get(6)) else "Fail") # returns 7
