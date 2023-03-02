class ErrorByByte(Exception):
    def __init__(self, err):
        self.err = err

words = ['attribute', 'класс', 'функция', 'type']

for word in words:
    word_b = bytes(word, 'ascii', 'ignore')
    try:
        if word_b == b'':
            raise ErrorByByte(
                f'{word}  - запись в байтовом типе невозможна')
        print(word_b)
    except ErrorByByte as err:
        print(err)