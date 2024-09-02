class Scorer:
    maximum_index_to_check : int = 5

    @staticmethod
    def check_score(original: str, checked: str) -> int :
        len_original: int = len(original)
        len_checked: int = len(checked)
        score: int = (len_original - 1) * 2
        multiplier: int = 2 if (len_original != len_checked) else 1
        max_index: int = min(len_original, Scorer.maximum_index_to_check)
        for i in range(0, max_index):
            if (original[i] != checked[i] or (len_original != len_checked and i == max_index - 1)):
                return score + ((i - Scorer.maximum_index_to_check) * multiplier)
        return score + 2


