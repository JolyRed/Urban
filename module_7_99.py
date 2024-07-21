def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, "w", encoding="utf-8") as f:
        for string in strings:
            position = f.tell()
            f.write(string + "\n")
            strings_positions[(f.tell() - len(string) - 1, position)] = string
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
