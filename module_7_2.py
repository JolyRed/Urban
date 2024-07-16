def custom_write(file_name, strings):
  with open(file_name, 'w', encoding='utf-8') as file:
    strings_positions = {}
    for string in strings:
      start_pos = file.tell()
      file.write(string + '\n')
      end_pos = file.tell()
      strings_positions[(file.lineno, start_pos)] = string
  return strings_positions
