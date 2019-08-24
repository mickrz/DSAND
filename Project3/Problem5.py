import collections


## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
        
    def suffixes(self, node):
        visit_order = list([])
        
        def traverse(root_node, suffix=''):
            for char, node in root_node.items():
                if node.is_word:
                    visit_order.append(suffix + char + " ")
                traverse(node.children, suffix + char)

        traverse(self.children)    
        return visit_order   
       
    
## The Trie itself containing the root node and insert/find functions
class Trie(object):
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root

        for char in word:
            current_node = current_node.children[char]
        current_node.is_word = True
            
    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]

        return current_node
    
    def suffixes(self, prefix):
        root_node = self.find(prefix)
        suffixes =  root_node.suffixes(root_node.children)
        return "".join(suffixes).strip(" ").split(" ")

        
        
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
    
   
print ("Pass" if ("hology, agonist, onym" == ", ".join(MyTrie.suffixes("ant"))) else "Fail")
print ("Pass" if ("un, unction, actory" == ", ".join(MyTrie.suffixes("f"))) else "Fail")
print ("Pass" if ("rie, rigger, rigonometry, ripod" == ", ".join(MyTrie.suffixes("t"))) else "Fail")
print ("Pass" if ("ger, onometry" == ", ".join(MyTrie.suffixes("trig"))) else "Fail")