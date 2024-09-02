from dataclasses import dataclass


@dataclass
class AutoCompleteData:
    """Class representing suggested auto completion for prompts"""

    complete_sentence: str
    source_text: str
    offset: int
    score: int