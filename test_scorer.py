import pytest
from scorer import Scorer


class TestScorer:
    @pytest.fixture(autouse=True)
    def setup(self):
        pass

    def test_equal_strings(self):
        string: str = "hello"
        assert Scorer.check_score(string, string) == len(string) * 2
        string: str = "hell"
        assert Scorer.check_score(string, string) == len(string) * 2
        string: str = "helloo"
        assert Scorer.check_score(string, string) == len(string) * 2
    
    def test_replaced(self):
        user_input: str = "hello"
        database_string: str = "vello"
        assert Scorer.check_score(user_input, database_string) == 3
        user_input = "hello"
        database_string = "heilo"
        assert Scorer.check_score(user_input, database_string) == 5
        user_input = "hellox"
        database_string = "helloo"
        assert Scorer.check_score(user_input, database_string) == 9
        user_input = "this is a"
        database_string = "this is b"
        assert Scorer.check_score(user_input, database_string) == 15


class TestTopFive:
    best: list[str] = Scorer.get_best_words("hello", ["hello", "hellov", "vello", "hellg", "ohello", "heilo"], 5)
    assert "ohello" not in best


if __name__ == "__main__":
    pytest.main()
