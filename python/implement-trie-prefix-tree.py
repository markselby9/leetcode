class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = ''
        self.children = {}

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if len(word) == 0: return
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
                continue
            new_node = TrieNode()
            new_node.val = c
            node.children[c]=new_node
            node = new_node
        node.children['eof'] = 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if len(word) == 0: return False
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        if 'eof' in node.children: return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if len(prefix) == 0: return False
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

# Your Trie object will be instantiated and called as such:
trie = Trie()
print trie.startsWith("hello")
trie.insert("somestring")
trie.insert("hello")
trie.insert("helloworld")
print trie.search("hello")
print trie.search("key")
print trie.startsWith("hello")
print trie.startsWith("helloworld")