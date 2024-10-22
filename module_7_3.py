import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        self.all_words = self._get_all_words()

    def _get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            words = []
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    line = line.translate(str.maketrans('', '', string.punctuation))
                    words.extend(line.split())
            all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        for name, words in self.all_words.items():
            if word in words:
                result[name] = words.index(word) + 1  # +1 для отсчета с 1, а не с 0
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        for name, words in self.all_words.items():
            result[name] = words.count(word)
        return result

# Пример использования
finder2 = WordsFinder('test_file.txt')
print(finder2.all_words)  # Все слова
print(finder2.find('text'))  # Позиция первого вхождения слова
print(finder2.count('text'))  # Количество вхождений слова в тексте
