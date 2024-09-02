from typing import List
import cProfile


END_PROMPT = "#"
END_PROGRAM = "quit"


# TODO: change to fit format of actual `suggestion` object (AutoCompleteData), not just string
def display_suggestions(suggestions: List[str]) -> None:
    """Prints all suggestions in given order and their meta data.

    Args:
        suggestions (List[str]): list of suggestions objects (AutoCompleteData object).
    """
    for i, suggestion in enumerate(suggestions, start=1):
        print(f"{i}. {suggestion}")


def main() -> None:
    """Main function for user interaction."""

    print("System is booting. Please wait...\n")
    ### init the system ###
    print("System is ready. Enter your text:\n")

    prompt = ""
    while True:
        # suggestions = <<< insert logic here >>> if prompt else []
        suggestions = ["suggestion 1", "suggestion 2"] if prompt else []
        
        display_suggestions(suggestions)

        print(f"\n{prompt}", end="")
        added = input()
        
        if added.strip() == END_PROMPT:
            prompt = ""
        
        elif added.strip() == END_PROGRAM:
            print("Exit...")
            break
        else:
            prompt += added


if __name__ == "__main__":
    cProfile.run('main()', sort='tottime')
