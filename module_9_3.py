first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(first_word) - len(second_word)
                for first_word, second_word in zip(first, second)
                if len(first_word) != len(second_word))

second_result = (first[i] == second[i]
                 for i in range(len(first)))
                

print(list(first_result))
print(list(second_result))
