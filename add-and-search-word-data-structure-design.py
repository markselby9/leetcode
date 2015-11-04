class Node(object):
    def __init__(self):
        self.val = ''
        self.children = {}

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if len(word) == 0: return 0
        node = self.root
        for w in word:
            if w in node.children:
                node = node.children[w]
            else:
                new_node = Node()
                new_node.val = w
                node.children[w] = new_node
                node = new_node
        node.children['eof'] = 1

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if len(word) == 0: return 0
        node = self.root
        return self.searchNode(word, node)

    def searchNode(self, word, node):
        # print word
        if len(word) == 0:
            if 'eof' in node.children: return True
            else: return False
        if word[0] == '.':
            result = False
            for child in node.children.values():
                if child!=1:    result |= self.searchNode(word[1:], child)
            return result
        else:
            if word[0] in node.children:
                return self.searchNode(word[1:], node.children[word[0]])
            else: return False
        # return False


# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("word")
wordDictionary.addWord("work")
wordDictionary.addWord("worst")
print wordDictionary.search("pattern")
print wordDictionary.search("work")
print wordDictionary.search("....")
print wordDictionary.search("...")
print wordDictionary.search("...se")