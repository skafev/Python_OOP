import random


class RandomList(list):
    def get_random_element(self):
        random_element = random.choice(self)
        random_element_index = [element for element in range(len(self)) if self[element] == random_element][0]
        self.pop(random_element_index)
        return random_element


# test first zero
import unittest
from unittest import mock
import random

class RandomListTests(unittest.TestCase):
    def test_zero_first(self):
        mocked_choice = lambda x: 5
        with mock.patch('random.choice', mocked_choice):
            li = RandomList()
            li.append(4)
            li.append(3)
            li.append(5)
            self.assertEqual(li.get_random_element(), 5)

if __name__ == '__main__':
    unittest.main()