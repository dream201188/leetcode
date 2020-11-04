#自己实现try树，完全没有按照概念
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.repo = list()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        self.repo.append(word)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return word in self.repo

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        a = [True for word in self.repo if prefix in word]
        return len(a) == 1


#按照标准概念
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.repo = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.repo
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['#'] = '#'

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.repo
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return '#' in node

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.repo
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True
