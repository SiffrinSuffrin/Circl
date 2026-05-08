class Program:
    def __init__(self):
        self.counters: list[int] = []

    def get_counter(self) -> int:
        return self.counters[-1]

    def add_counter(self):
        self.counters.append(0)

    def remove_counter(self):
        _ = self.counters.pop()

    def increment_counter(self, increment: int = 1):
        self.counters[-1] += increment

    def decrement_counter(self, decrement: int = 1):
        self.counters[-1] -= decrement

    def set_counter(self, counter: int):
        self.counters[-1] = counter

    def number_of_counters(self):
        return len(self.counters)


main_program: Program = Program()
