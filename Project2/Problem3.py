import sys
from operator import itemgetter

class Node(object):
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
        
    def set_value(self, value):
        self.value = value
    
    def get_value(self):
        return self.value
    
    def set_left_child(self, child):
        self.left = child
        
    def set_right_child(self, child):
        self.right = child
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right
    
    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None

    def __repr__(self):
        return f"Node({self.get_value()}, {self.has_left_child()}, {self.has_right_child()})"
    
    def __str__(self):
        return f"Node({self.get_value()}, {self.has_left_child()}, {self.has_right_child()})"

class Tree(object):
    def __init__(self):
        self.root = None
        
    def set_root(self, value):
        self.root = value
        
    def get_root(self):
        return self.root
    
    
huffman_freq = dict({})
huffman_tree = Tree()
huffman_code = dict({})

def generate_frequencies(data):
    for letter in data:
        if letter in huffman_freq:
            huffman_freq[letter] += 1
        else:
            huffman_freq[letter] = 1
    return huffman_freq


def build_huffman_tree(char_freqs):
    # create nodes ahead of time to build the tree
    char_values = char_freqs
    root_node = None

    while len(char_values) > 1:
        char1, freq1 = char_values[-1]
        char2, freq2 = char_values[-2]
        char_values = char_values[:-2]
        new_node = Node()
        new_node.set_left_child(char1)
        new_node.set_right_child(char2)
        char_values.append((new_node, freq1 + freq2))
        # Re-sort the list
        char_values.sort(key=itemgetter(1), reverse = True)
        root_node = new_node
    huffman_tree.set_root(root_node)    
    return root_node


def traverse_huffman_tree(node, code=''):
    if type(node) is str:
        return {node: code}
    
    left_node = node.get_left_child()
    right_node = node.get_right_child()
    
    huffman_code.update(traverse_huffman_tree(left_node, code + "0"))
    huffman_code.update(traverse_huffman_tree(right_node, code + "1"))
    return huffman_code


def process(data):
    # generate frequencies and sort
    freq_list = list(generate_frequencies(data).items())
    freq_list.sort(key=itemgetter(1), reverse = True)

    # build tree bottom-up and create codes
    traverse_huffman_tree(build_huffman_tree(freq_list))

    
def huffman_encoding(data):
    if len(data) == 0:
        return "There was no message encoded as original string is empty!", None

	encoded_string = ''    
    process(data)
    
    # use lookup map to encode instead of traversing tree
    for char in data:
        encoded_string += huffman_code[char]

    return encoded_string, huffman_tree

def decode_message(data, node):
    if type(node) is str:
        return data, node
    
    if data[0] == "0" and node.has_left_child():
        return decode_message(data[1:], node.get_left_child())
    elif data[0] == "1" and node.has_right_child():
        return decode_message(data[1:], node.get_right_child())


def huffman_decoding(data, huffman_tree):
    decoded_msg = '' 

    # traverse tree for each char
    while len(data) > 0:
        data, char = decode_message(data, huffman_tree.get_root())
        decoded_msg += char

    return decoded_msg


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    another_string = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    print ("The size of the data is: {}\n".format(sys.getsizeof(another_string)))
    print ("The content of the data is: {}\n".format(another_string))

    encoded_data, tree = huffman_encoding(another_string)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    yet_another_string = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    print ("The size of the data is: {}\n".format(sys.getsizeof(yet_another_string)))
    print ("The content of the data is: {}\n".format(yet_another_string))

    encoded_data, tree = huffman_encoding(yet_another_string)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    yet_one_last_string = ""
    print ("The size of the data is: {}\n".format(sys.getsizeof(yet_one_last_string)))
    print ("The content of the data is: {}\n".format(yet_one_last_string))

    encoded_data, tree = huffman_encoding(yet_one_last_string)

    if tree is not None:
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))
    else:
        print(encoded_data)	