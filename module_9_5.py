class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self
        
    def __next__(self):
        if (self.step > 0 and self.pointer >= self.stop) or (self.step < 0 and self.pointer <= self.stop):
            raise StopIteration
        self.pointer += self.step
        return self.pointer - self.step
