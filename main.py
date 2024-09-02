import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'CoreLogic')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'TextHandling')))
from TextHandling import reader, cleaner
from CoreLogic import BK_Tree, HashTable

def offline():
    bk_tree = BK_Tree.BKTree()
    hash_table = HashTable.HashTable()

    read = reader.TxtReader()
    reader_generator = read.read_lines("C:\\Users\\Saleh\\ScaleUpExelantem\\GoogleAutoCompleteProject\\Archive\\rfc7501.txt")

    # Get the path first
    file_path = next(reader_generator)
    file_name = os.path.basename(file_path)  # Extract just the file name

    line_counter = 0

    for line in reader_generator:
        line_counter += 1
        cleaned_line = cleaner.clean_line(line)
        words = cleaned_line.split()
        for offset, word in enumerate(words, start=1):
            word_lower = word.lower()
            bk_tree.insert(word_lower)
            hash_table.insert_data(word_lower, file_name, line_counter, offset)

    bk_tree.save_to_json("bk_tree.json")
    hash_table.save_to_json("hash_table.json")

if __name__ == '__main__':
    # Run the offline function to populate and save the data structures
    offline()

    # Load the HashTable
    hash_table = HashTable.HashTable.load_from_json("hash_table.json")

    # Search in BKTree
    result = BK_Tree.search_in_tree("bk_tree.json", "must", 1)
    result2 = BK_Tree.search_in_tree("bk_tree.json", "includ", 1)

    print(f"Search result 1: {result[0]}")
    print(f"Search result 2: {result2[0]}")

    # Ensure the search results are processed consistently
    key = hash_table.find_sentence([result[0].lower(), result2[0].lower()], 0.75)
    print(f"Best key found: {key}")

    if not key:
        print(f"Words to search: {[result[0].lower(), result2[0].lower()]}")
        for word in [result[0].lower(), result2[0].lower()]:
            data = hash_table.get_data(word)
            print(f"Data for word '{word}': {data}")
