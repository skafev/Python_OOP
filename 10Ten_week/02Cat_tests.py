import unittest


class CatTests(unittest.TestCase):
    """   Cat's size is increased after eating
   Cat is fed after eating
   Cat cannot eat if already fed, raises an error
   Cat cannot fall asleep if not fed, raises an error
   Cat is not sleepy after sleeping"""

    # Case1
    def test_cat_size_correctly_increased_after_eating(self):
        name = "Gosho"
        cat = Cat(name)
        cat.eat()
        self.assertEqual(1, cat.size)

    # Case2
    def test_after_eating_should_return_fed_to_be_true(self):
        name = "Gosho"
        cat = Cat(name)
        cat.eat()
        self.assertEqual(True, cat.fed)

    # Case3
    def test_cat_when_fed_cannot_eat_error_raise(self):
        name = "Gosho"
        cat = Cat(name)
        cat.fed = True
        with self.assertRaises(Exception):
            cat.eat()

    # Case4
    def test_cat_cannot_sleep_if_not_fed_working(self):
        name = "Gosho"
        cat = Cat(name)
        with self.assertRaises(Exception):
            cat.sleep()

    # Case5
    def test_cat_sleepy_after_sleep_should_be_false(self):
        name = "Gosho"
        cat = Cat(name)
        cat.sleepy = True
        cat.fed = True
        cat.sleep()
        self.assertEqual(False, cat.sleepy)


if __name__ == '__main__':
    unittest.main()
