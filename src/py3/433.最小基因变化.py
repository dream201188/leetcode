class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        word_set = set(bank)
        level = [start]
        level_num = -1
        new_chars = ['A', 'C', 'G', 'T']

        while level:
            level_num += 1
            new_level = []
            for curr_word in level:
                if curr_word == end:
                    return level_num
                for i, char in enumerate(curr_word):
                    for new_char in new_chars:
                        if char == new_char:
                            continue
                        new_word = curr_word[:i] + new_char + curr_word[i + 1:]
                        if new_word in word_set:
                            new_level.append(new_word)
                            word_set.remove(new_word)
            level = new_level[:]
        return -1

    def minMutation(self, start, end, bank):

        # 双向BFS 不增加这个特殊判断过不了
        if not bank or end not in bank:
            return -1

        word_set = set(bank)
        start_set = {start}
        end_set = {end}
        level_num = 0  # 与单项比这个少一层
        new_chars = ['A', 'C', 'G', 'T']

        while start_set:
            level_num += 1
            new_level = set()
            for curr_word in start_set:
                for i, char in enumerate(curr_word):
                    for new_char in new_chars:
                        if char == new_char:
                            continue
                        new_word = curr_word[:i] + new_char + curr_word[i + 1:]
                        if new_word in end_set:
                            return level_num
                        if new_word in word_set:
                            new_level.add(new_word)
                            word_set.remove(new_word)
            start_set = new_level
            if len(start_set) > len(end_set):
                start_set, end_set = end_set, start_set
        return -1




