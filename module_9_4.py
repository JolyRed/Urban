import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))

print(result)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:  
            f.write('\n'.join(str(data) for data in data_set))  
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def call(self):
        return random.choice(self.words)
    

ball = MysticBall('Да', 'Нет', 'Наверное')
print(ball.call())
print(ball.call())
print(ball.call())
