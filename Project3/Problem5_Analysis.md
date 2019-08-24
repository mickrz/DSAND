# Problem Description:
## Building a Trie in Python
Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.

Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
* A `Trie` class that contains the root node (empty string)
* A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.

## Finding Suffixes
Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.

Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

## Testing it all out
Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

`python
print ("Pass" if ("hology, agonist, onym" == ", ".join(MyTrie.suffixes("ant"))) else "Fail")
print ("Pass" if ("un, unction, actory" == ", ".join(MyTrie.suffixes("f"))) else "Fail")
print ("Pass" if ("rie, rigger, rigonometry, ripod" == ", ".join(MyTrie.suffixes("t"))) else "Fail")
print ("Pass" if ("ger, onometry" == ", ".join(MyTrie.suffixes("trig"))) else "Fail")
`


# Analysis:
## Time Complexity:
The time complexity is split into there for `insert`, `find` and `suffixes`. Refer Design Choices section.

## Space Complexity:
The space complexity is split into there for `insert`, `find` and `suffixes`. Refer Design Choices section.

## Design Choices:
I used a Trie with DFS In-order search. This was tricky, but the best way to approach this problem since we had to traverse all the nodes for a given input prefix to find all the suffixes related to it.
Time complexity for `insert` and `find` is O(n) to loop through each char in word.
Space complexity for `insert` and `find` is O(mn) where m is the word inserting/finding and n is the total number of words.

Time complexity for `suffixes` is O(V + E) where V is the vertices and E is the edges. In theory, each branch could be traversed.
Space complexity for `suffixes` is O(bm) where b is the branches to travel and m is the longest word.