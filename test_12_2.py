import unittest

class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed
    def walk(self):
        self.distance += self.speed // 2 

    def __str__(self):
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
        while self.participants:
            for participant in self.participants[:]: 
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[len(finishers) + 1] = participant
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Usain", speed=10)
        self.runner2 = Runner("Andrey", speed=9)
        self.runner3 = Runner("Nick", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_usain_nick(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertEqual(list(results.values())[-1].name, "Nick")

    def test_andrey_nick(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertEqual(list(results.values())[-1].name, "Nick")

    def test_usain_andrey_nick(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertEqual(list(results.values())[-1].name, "Nick")


if __name__ == '__main__':
    unittest.main()
