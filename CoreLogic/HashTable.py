import json

class HashTable:
    def __init__(self):
        # Initialize the hash table as an empty dictionary
        self.HashTable = {}

    def insert_data(self, Word: str, FileName: str, LineNumber: int, OffSet: int):
        # Compute the hash index
        index = hash(Word)

        # Check if the index is already in the dictionary
        if index not in self.HashTable:
            # If not, initialize an empty list for this index
            self.HashTable[index] = []

        # Append the data tuple to the list at this index
        self.HashTable[index].append((FileName, LineNumber, OffSet))

    def get_data(self, Word: str) -> list[tuple[str, int, int]]:
        # Compute the hash index
        index = hash(Word)

        # Return the list of data tuples stored at this index
        # If the index doesn't exist, return an empty list
        return self.HashTable.get(index, [])

    def find_sentence(self, words: list[str], threshold: float = 0.8) -> list[tuple[str, int]]:
        best_key = None  # To store the best (filename, line number) key

        # Create a dictionary to store the positions by filename and line number
        positions = {}

        total_words = len(words)
        if total_words == 0:
            return []

        for word in words:
            word_data = self.get_data(word)
            for FileName, LineNumber, OffSet in word_data:
                if (FileName, LineNumber) not in positions:
                    positions[(FileName, LineNumber)] = []
                positions[(FileName, LineNumber)].append((OffSet, word))

        # Process each filename and line number group
        for (FileName, LineNumber), offsets in positions.items():
            # Sort offsets based on the OffSet value
            offsets.sort(key=lambda x: x[0])

            continuous_sentence = []
            previous_offset = None
            matched_words = 0
            best_matched_words = 0

            for offset, word in offsets:
                if previous_offset is None or offset == previous_offset + 1:
                    continuous_sentence.append(word)
                    matched_words += 1
                else:
                    # If the sequence is broken, compare with the best sequence found so far
                    if matched_words > best_matched_words and matched_words / total_words >= threshold:
                        best_key = (FileName, LineNumber)
                        best_matched_words = matched_words

                    # Reset for the new sequence
                    continuous_sentence = [word]
                    matched_words = 1

                previous_offset = offset

            # Final check after loop to update the best key
            if matched_words > best_matched_words and matched_words / total_words >= threshold:
                best_key = (FileName, LineNumber)

        # Return the best key (filename, line number)
        return [best_key] if best_key else []

    def save_to_json(self, file_path: str):
        # Convert the HashTable to a serializable format
        serializable_table = {str(key): value for key, value in self.HashTable.items()}
        with open(file_path, 'w') as f:
            json.dump(serializable_table, f)

    @staticmethod
    def load_from_json(file_path: str):
        # Load the hash table from a JSON file
        with open(file_path, 'r') as f:
            data = json.load(f)
        loaded_table = HashTable()
        # Convert string keys back to their original type (int)
        loaded_table.HashTable = {int(key): value for key, value in data.items()}
        return loaded_table

