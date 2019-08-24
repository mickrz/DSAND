# Problem Description:
## Huffman Coding
A Huffman code is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.

The Huffman algorithm works by assigning codes that correspond to the relative frequency of each character for each character. The Huffman code can be of any length and does not require a prefix; therefore, this binary code can be visualized on a binary tree with each encoded character being stored on leafs.

There are many types of pseudocode for this algorithm. At the basic core, it is comprised of building a Huffman tree, encoding the data, and, lastly, decoding the data.

Here is one type of pseudocode for this coding schema:

* Take a string and determine the relevant frequencies of the characters.
* Build and sort a list of tuples from lowest to highest frequencies.
* Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)
* Trim the Huffman Tree (remove the frequencies from the previously built tree).
* Encode the text into its compressed form.
* Decode the text from its compressed form.
* You then will need to create encoding, decoding, and sizing schemas.


# Analysis:
## Time Complexity:
The time complexity is `O(nlog(n))`. Refer Design Choices section.

## Space Complexity:
The space complexity is `O(n)`. `O(n)` for each map and DFS is `O(|V|)`.

## Design Choices:
I spent a lot of time on this problem. Conceptually after a few YouTube videoes, it's easy to understand but I still had to draw it out on paper a few times. As a samples steps mention, first I got the frequencies of the characters, sort them, create nodes starting with the least frequent chars to build a tree and finally traverse the tree to generate the codes. With the generated codes, I used that to encode the message and to decode, I had to traverse the tree using the bits to go left or right down until hitting a char. One thing I forgot to include is the sort which takes O(nlog(n)).

For time complexity, I used two dictionaries - (1) for frequencies and (2) for codes. It made for O(1) lookups. To traverse the tree (DFS) and recursion - O(V+E) where V = vertices and E = edges.