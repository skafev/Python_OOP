import unittest

class IntegerListTests(unittest.TestCase):
    """add operation, should add an element and returns the list.
        If the element is not an integer, a ValueError is thrown"""

    # Case1
    def test_add_method_should_return_correct_list_of_integers(self):
        my_list = IntegerList(1, 2, 3, 4)
        my_list.add(5)
        self.assertEqual([1, 2, 3, 4, 5], my_list.get_data())

    # Case2
    def test_add_element_not_integer_expect_value_error(self):
        my_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            my_list.add("asd")

    # remove_index operation removes the element on that index and returns it.
    # If the index is out of range, an IndexError is thrown

    # Case3
    def test_remove_index_removes_the_element_and_returns_it_correctly(self):
        value_to_remove = 3
        my_list = IntegerList(1, 2, value_to_remove, 4)
        result = my_list.remove_index(2)
        self.assertEqual(value_to_remove, result)
        self.assertListEqual([1, 2, 4], my_list.get_data())

    # Case4
    def test_remove_index_the_element_index_gives_index_error(self):
        my_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(IndexError):
            my_list.remove_index(5)

    # __init__ should only take integers, and store them

    # Case5
    def test_verify_init_method_to_take_only_ints_and_store_them(self):
        IntegerList(1, 2, 3, 4)

    # # Case6
    # def test_init_when_not_only_integers_are_passed_raise_exception(self):
    #     with self.assertRaises(Exception):
    #         IntegerList(1, 2, 3, "asdas")

    # • get should return the specific element
    #     ◦ If the index is out of range, an IndexError is thrown
    # Case7
    def test_when_get_method_called_should_return_correct_element_from_given_index(self):
        my_list = IntegerList(1, 2, 3, 4)
        index = 3
        result = my_list.get(index)
        self.assertEqual(4, result)

    # Case8
    def test_when_get_method_called_index_out_of_range_index_error_expected(self):
        my_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(IndexError):
            my_list.get(5)

    # • insert
    #     ◦ If the index is out of range, IndexError is thrown
    #     ◦ If the element is not an integer, ValueError is thrown

    def test_insert_method_working_correctly(self):
        my_list = IntegerList(1, 2, 3, 4)
        index = 0
        element = 0
        my_list.insert(index, element)

    def test_when_insert_method_get_integer_that_is_out_of_range_index_error_expected(self):
        my_list = IntegerList(1, 2, 3, 4)
        index = 6
        element = 0
        with self.assertRaises(IndexError):
            my_list.insert(index, element)

    def test_when_insert_method_get_element_that_is_not_integer_value_error_expected(self):
        my_list = IntegerList(1, 2, 3, 4)
        index = 0
        element = "asd"
        with self.assertRaises(ValueError):
            my_list.insert(index, element)

    # • get_biggest
    # • get_index

    def test_get_biggest_method_return_biggest_number(self):
        my_list = IntegerList(1, 2, 3, 4)
        result = my_list.get_biggest()
        self.assertEqual(4, result)

    def test_get_index_method_return_index_correctly(self):
        my_list = IntegerList(1, 2, 3, 4)
        element = 3
        result = my_list.get_index(3)
        self.assertEqual(2, result)


if __name__ == '__main__':
    unittest.main()
