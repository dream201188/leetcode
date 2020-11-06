class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        from collections import deque
        word_set = set(wordList)
        queue = deque()
        queue.append((beginWord, 1))
        while (queue):
            curr = queue.popleft()
            if curr[0] == endWord:
                return curr[1]
            curr_word = curr[0]
            level = curr[1]
            for i, char in enumerate(curr_word):
                for j in range(97, 123):
                    if char == chr(j):
                        continue
                    new_word = curr_word[0:i] + chr(j) + curr_word[i + 1:]
                    if new_word in word_set:
                        queue.append((new_word, level + 1))
                        word_set.remove(new_word)
        return 0

    # 典型的层序遍历
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        from collections import deque
        word_set = set(wordList)
        queue = deque()
        queue.append(beginWord)
        level = 0
        while (queue):
            level += 1
            for i in range(len(queue)):
                curr_word = queue.popleft()
                if curr_word == endWord:
                    return level
                for i, char in enumerate(curr_word):
                    for j in range(97, 123):
                        if char == chr(j):
                            continue
                        new_word = curr_word[0:i] + chr(j) + curr_word[i + 1:]
                        if new_word in word_set:
                            queue.append(new_word)
                            word_set.remove(new_word)
        return 0
