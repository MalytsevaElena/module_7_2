# Задача "Записать и запомнить"

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding= 'utf-8')
    strings_positions = {}
    for i in range(0, len(strings)):
        strings_positions.update({(i+1, file.tell()): strings[i]})
        file.write('\n'+ strings[i])
    file.close()
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
