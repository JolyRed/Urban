import unittest

def skip_if_frozen(test_func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            print("Тесты в этом кейсе заморожены")
            raise unittest.SkipTest("Тесты в этом кейсе заморожены")
        return test_func(self, *args, **kwargs)
    return wrapper

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

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
        place = 1
        
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
            if len(finishers) == 0:
                break

        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False 

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("Walker")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        runner = Runner("Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")
        
        for _ in range(10):
            runner1.run()
            runner2.walk()
        
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_first_tournament(self):
        runner1 = Runner("Usain", speed=10)
        runner2 = Runner("Nick", speed=3)
        tournament = Tournament(90, runner1, runner2)
        results = tournament.start()
        self.assertEqual(list(results.values())[-1].name, "Nick")

    @skip_if_frozen
    def test_second_tournament(self):
        runner1 = Runner("Andrey", speed=9)
        runner2 = Runner("Nick", speed=3)
        tournament = Tournament(90, runner1, runner2)
        results = tournament.start()
        self.assertEqual(list(results.values())[-1].name, "Nick")

    @skip_if_frozen
    def test_third_tournament(self):
        runner1 = Runner("Usain", speed=10)
        runner2 = Runner("Andrey", speed=9)
        runner3 = Runner("Nick", speed=3)
        tournament = Tournament(90, runner1, runner2, runner3)
        results = tournament.start()
        self.assertEqual(list(results.values())[-1].name, "Nick")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RunnerTest))
    suite.addTest(unittest.makeSuite(TournamentTest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
