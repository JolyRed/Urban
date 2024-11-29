import logging
import unittest

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        
        self.distance = 0
        
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers




logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w', encoding='UTF-8',
                    format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    try:
        runner1 = Runner("Usain", speed=10)
        runner1.run()
        print(f"Бегун {runner1} пробежал {runner1.distance} метров.")
        
        runner2 = Runner(123, speed=3)  
    except TypeError as e:
        logging.warning(f"Ошибка при создании Runner: {e}")
    except ValueError as e:
        logging.warning(f"Ошибка при создании Runner: {e}")

    tournament = Tournament(100, Runner("Bob"), Runner("Alice"))
    winners = tournament.start()
    print("Победители турнира:")
    for place, winner in winners.items():
        print(f"{place} место: {winner}")

    unittest.main(verbosity=2)



