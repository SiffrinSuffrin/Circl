import unittest

from Program import Program


class TestInstructionSet(unittest.TestCase):
    pass

class TestCircl(unittest.TestCase):
    pass

class TestInterpreter(unittest.TestCase):
    pass

class TestProgram(unittest.TestCase):
    def setUp(self):
        self.program = Program()
    def tearDown(self):
        del self.program

    def test_initialization(self):
        self.assertEqual(self.program.counters, [])
        self.assertEqual(self.program.number_of_counters(), 0)

    def test_adding_and_removing_counters(self):
        self.assertEqual(self.program.counters, [])
        self.program.add_counter()
        self.assertEqual(self.program.counters, [0])
        self.program.remove_counter()
        self.assertEqual(self.program.counters, [])

        self.program.counters = [1,2,3,4,5,6]
        self.program.add_counter()
        self.program.add_counter()
        self.assertEqual(self.program.counters, [1,2,3,4,5,6,0,0])
        for i in range(4):
            self.program.remove_counter()
        self.assertEqual(self.program.counters, [1,2,3,4])

    def test_incrementing_decrementing_setting_counters(self):
        self.program.counters = [1,2,3,4,5,6]
        self.program.increment_counter()
        self.assertEqual(self.program.counters, [1,2,3,4,5,7])
        self.program.increment_counter()
        self.assertEqual(self.program.counters, [1, 2, 3, 4, 5, 8])
        self.program.set_counter(25)
        self.assertEqual(self.program.counters, [1, 2, 3, 4, 5, 25])
        for i in range(4):
            self.program.decrement_counter()
        self.assertEqual(self.program.counters, [1, 2, 3, 4, 5, 21])
        self.program.remove_counter()
        self.program.remove_counter()
        self.program.remove_counter() #[1, 2, 3]
        for i in range(10):
            self.program.increment_counter()
        self.assertEqual(self.program.counters, [1, 2, 13])
        for i in range(15):
            self.program.decrement_counter()
        self.assertEqual(self.program.counters, [1, 2, -2])
        self.program.set_counter(-42)
        self.assertEqual(self.program.counters, [1, 2, -42])


    def test_getting_counter(self):
        self.program.counters = [1,2,3,4,5,6]
        self.assertEqual(self.program.get_counter(), 6)
        self.program.counters = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(self.program.get_counter(), 8)
        self.program.counters = [1, 2, 3]
        self.assertEqual(self.program.get_counter(), 3)

if __name__ == '__main__':
    unittest.main()