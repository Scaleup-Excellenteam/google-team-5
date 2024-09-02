class HashTable:
    def __init__(self, HashFunc):
        self.hashFunc = HashFunc
        self.HashTable = []

    def insert_data(self, Word: str, FileName: str, LineNumber: int, OffSet: int):
        index = self.hashFunc(Word)
        self.HashTable[index].append((FileName, LineNumber, OffSet))

    def get_data(self, Word: str) -> tuple[str, int, int]:
        index = self.hashFunc(Word)
        return self.HashTable[index]