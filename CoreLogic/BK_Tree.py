import json

class BKTreeNode:
    def __init__(self, word):
        self.word = word
        self.children = {}  # Dictionary to hold children, keyed by the difference count

    def to_dict(self):
        result = {'word': self.word, 'children': {}}
        stack = [(result['children'], self.children)]

        while stack:
            current_dict, children = stack.pop()
            for k, v in children.items():
                child_dict = {'word': v.word, 'children': {}}
                current_dict[k] = child_dict
                if v.children:
                    stack.append((child_dict['children'], v.children))

        return result

    @staticmethod
    def from_dict(data):
        node = BKTreeNode(data['word'])
        node.children = {int(k): BKTreeNode.from_dict(v) for k, v in data['children'].items()}
        return node


class BKTree:
    def __init__(self, max_depth=1000):
        self.root = None
        self.max_depth = max_depth

    def insert(self, word):
        if self.root is None:
            self.root = BKTreeNode(word)
            return

        current_node = self.root
        current_depth = 0

        while current_depth < self.max_depth:
            diff_count = self.diff_count(current_node.word, word.lower())

            if diff_count == 0:
                # Word is identical, no need to insert
                return

            if diff_count in current_node.children:
                # Move to the child node with the same diff_count
                current_node = current_node.children[diff_count]
            else:
                # Insert the word as a new child if no child exists with the same diff_count
                current_node.children[diff_count] = BKTreeNode(word)
                return

            current_depth += 1

    def diff_count(self, s1, s2):
        differences = sum(1 for a, b in zip(s1, s2) if a != b)
        return differences + abs(len(s1) - len(s2))

    def to_dict(self):
        return self.root.to_dict() if self.root else None

    def save_to_json(self, file_path):
        with open(file_path, 'w') as f:
            json.dump(self.to_dict(), f)

    @staticmethod
    def load_from_json(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
        tree = BKTree()
        tree.root = BKTreeNode.from_dict(data) if data else None
        return tree

    def search(self, word, max_distance=1):
        if self.root is None:
            return None
        else:
            return self._search_recursive(self.root, word.lower(), max_distance, None, max_distance + 1)

    def _search_recursive(self, node, word, max_distance, closest_word, closest_diff):
        diff_count = self.diff_count(node.word, word)

        if diff_count < closest_diff:
            closest_word = node.word
            closest_diff = diff_count

        if diff_count == 0:  # Exact match found
            return closest_word, closest_diff

        for d in range(diff_count - max_distance, diff_count + max_distance + 1):
            child = node.children.get(d)
            if child:
                closest_word, closest_diff = self._search_recursive(child, word, max_distance, closest_word,
                                                                    closest_diff)

        return closest_word, closest_diff


# Standalone function for searching the tree loaded from JSON
def search_in_tree(tree_file, word, max_distance=1):
    tree = BKTree.load_from_json(tree_file)
    return tree.search(word, max_distance)
