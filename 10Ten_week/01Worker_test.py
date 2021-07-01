import unittest


class WorkerTests(unittest.TestCase):
    """  Test if the worker is initialized with correct name, salary and energy
    Test if the worker's energy is incremented after the rest method is called
    Test if an error is raised if the worker tries to work with negative energy or equal to 0
    Test if the worker's money is increased by his salary correctly after the work method is called
    Test if the worker's energy is decreased after the work method is called
    Test if the get_info method returns the proper string with correct values"""

    # Case1
    def test_when_worker_init_is_correct(self):
        name = "Gosho"
        salary = 1000
        energy = 10
        worker = Worker(name, salary, energy)
        self.assertEqual(name, worker.name)
        self.assertEqual(salary, worker.salary)
        self.assertEqual(energy, worker.energy)

    # Case2
    def test_when_rest_worker_energy_incremented_properly(self):
        name = "Gosho"
        salary = 1000
        energy = 10
        worker = Worker(name, salary, energy)
        worker.rest()
        self.assertEqual(energy + 1, worker.energy)

    # Case3
    def test_when_worker_try_to_work_with_negative_energy_exception(self):
        name = "Gosho"
        salary = 1000
        energy = 0
        worker = Worker(name, salary, energy)
        with self.assertRaises(Exception):
            worker.work()

    # Case4
    def test_when_work_method_salary_correctly_increased(self):
        name = "Gosho"
        salary = 1000
        energy = 100
        worker = Worker(name, salary, energy)
        worker.work()
        self.assertEqual(worker.salary, worker.money)

    # Case5
    def test_when_work_method_called_energy_decreased_correctly(self):
        name = "Gosho"
        salary = 1000
        energy = 100
        worker = Worker(name, salary, energy)
        worker.work()
        self.assertEqual(energy - 1, worker.energy)

    # Case6
    def test_get_info_method_returns_correct_result(self):
        name = "Gosho"
        salary = 1000
        energy = 100
        worker = Worker(name, salary, energy)
        worker.money = 100
        worker.get_info()
        expect = f'{worker.name} has saved 100 money.'
        actual = worker.get_info()
        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
