class PrefixTree:

    def __init__(self):
        self.storage = {}

    def insert(self, word: str) -> None:
        ref = self.storage
        for char in word:
            if char in ref.keys():
                ref = ref[char]
            else:
                ref[char] = {}
                ref = ref[char]
        ref["*"] = True

    def search(self, word: str) -> bool:
        ref = self.storage
        for char in word:
            if char in ref.keys():
                ref = ref[char]
            else:
                return False
        if "*" in ref.keys():
            return True
        return False
        
    def startsWith(self, prefix: str) -> bool:
        ref = self.storage
        for char in prefix:
            if char in ref.keys():
                ref = ref[char]
            else:
                return False
        return True 
        