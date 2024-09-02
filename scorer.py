from heapq import heapify, heappush, heappushpop, nlargest

class Node:
    def __init__(self, given_str, correct_str):
        self.given = given_str
        self.score = Scorer.check_score(given_str, correct_str)

    def __lt__(self, other):
        return self.score < other.score


class MaxHeap():
    def __init__(self, top_n):
        self.h = []
        self.length = top_n
        heapify(self.h)
        
    def add(self, element):
        if len(self.h) < self.length:
            heappush(self.h, element)
        else:
            heappushpop(self.h, element)
            
    def getTop(self):
        return nlargest(self.length, self.h)

class Scorer:
    maximum_index_to_check : int = 5

    @staticmethod
    def check_score(original: str, checked: str) -> int :
        len_original: int = len(original)
        len_checked: int = len(checked)
        score: int = (len_original - 1) * 2
        multiplier: int = 2 if (len_original != len_checked) else 1
        max_index: int = min(len_original, Scorer.maximum_index_to_check)
        strings_equal: bool = original == checked
        for i in range(0, max_index):
            if (original[i] != checked[i] or (not strings_equal and i == max_index - 1)):
                return score + ((i - Scorer.maximum_index_to_check) * multiplier)
        return score + 2

    @staticmethod
    def get_best_words(correct, array: list[str], quantity: int) -> list[str]:
        result: MaxHeap = MaxHeap(quantity)
        ret: list[Node] = []
        for word in array:
            result.add(Node(word, correct))
        return result.getTop()
