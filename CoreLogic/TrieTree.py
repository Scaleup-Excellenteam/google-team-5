class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode(letter)
            node = node.children[letter]

    def search_complete_word(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return True

    def levenshtein_distance(self, word1, word2):
        len1, len2 = len(word1), len(word2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for i in range(len1 + 1):
            dp[i][0] = i
        for j in range(len2 + 1):
            dp[0][j] = j

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j],  # Deletion
                                       dp[i][j - 1],  # Insertion
                                       dp[i - 1][j - 1])  # Substitution

        return dp[len1][len2]

    def collect_words(self, node=None, prefix='', words=None):
        if words is None:
            words = []
        if node is None:
            node = self.root

        if node.children == {}:
            words.append(prefix)

        for letter, child_node in node.children.items():
            self.collect_words(child_node, prefix + letter, words)

        return words

    def find_most_similar_word(self, target_word):
        all_words = self.collect_words()
        most_similar_word = None
        min_distance = float('inf')

        for word in all_words:
            distance = self.levenshtein_distance(target_word, word)
            if distance < min_distance:
                min_distance = distance
                most_similar_word = word

        return most_similar_word

    def print_trie(self, node=None, level=0):
        if node is None:
            node = self.root

        if node.letter:
            print(" " * level * 2 + f"- {node.letter}")

        for child in node.children.values():
            self.print_trie(child, level + 1)

if __name__ == "__main__":
    trie = Trie()
    trie.insert("sad")
    trie.insert("sak")
    trie.insert("ssd")
    trie.insert("ffk")
    trie.insert("super")
    print(trie.find_most_similar_word("soker"))
