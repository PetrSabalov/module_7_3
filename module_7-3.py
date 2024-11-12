class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_words = {}

        for name in self.file_names:
            word = self._read_words(name)
            all_words[name] = word
        return all_words

    def _read_words(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read().lower()

            sym_to_remove = ',!?.:-'

            for symbol in sym_to_remove:
                text = text.replace(symbol, " ")
                words = text.split()
            return words

    def find(self, word):
        word_acc = {}

        for file_name, words in self.get_all_words().items():
            if word.lower() in words:
                position = words.index(word.lower()) + 1
                word_acc[file_name] = position

        return word_acc

    def count(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            count = words.count(word.lower())
            if count > 0:
                result[name] = count

        return result


finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))