class Scorer:
    maximum_index_to_check : int = 5

    @staticmethod
    def check_score(original: str, checked: str) -> int :
        len_original: int = len(original)
        len_checked: int = len(checked)
        score: int = (len_original - 1) * 2
        multiplier: int = 2 if (len_original != len_checked) else 1
        for i in range(0, min(len_original, Scorer.maximum_index_to_check)):
            if (original[i] != checked[i]):
                return score + ((i - Scorer.maximum_index_to_check) * multiplier)
        return score + 2
