words = [b'class', b'function', b'method']

for word in words:
    print(f'тип переменной:{type(word)}')
    print(f'содержание переменной - {word}')
    print(f'длина переменной: {len(word)} символов')
    print()