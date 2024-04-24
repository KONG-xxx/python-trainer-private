import sys
sys.path.append("..")

import unittest

# print(sys.path)
from project_0 import even_or_odd, multiplication_or_sum, add_and_iterate, reverse_str, remove_first_n_chars, check_n_same, save_divisible


class TestMultiplicationOrSum(unittest.TestCase):
    #@unittest.skip("")
    def test_less_thousand(self):
        self.assertEqual(multiplication_or_sum(20, 50), 70)

    #@unittest.skip("")
    def test_more_thousand(self):
        self.assertEqual(multiplication_or_sum(10, 50), 500)

# @unittest.skip("")
class TestEvenOrOdd(unittest.TestCase):
    def test_even(self):
        self.assertEqual(even_or_odd(2), 1)

    def test_odd(self):
        self.assertEqual(even_or_odd(1), 2)

    def test_non_num(self):
        self.assertEqual(even_or_odd("awdaw"), 0)
        self.assertEqual(even_or_odd(True), 0)


class TestArr(unittest.TestCase):
    # @unittest.skip("")
    def test_add_and_iterate(self):
        self.assertEqual(add_and_iterate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 55)

    # @unittest.skip("")
    def test_check_n_same(self):
        self.assertEqual(check_n_same([1, 2, 3, 4, 5, 6, 7, 8], [1, 1, 1, 1, 1, 2, 3], 3), True)
        self.assertEqual(check_n_same([1, 2, 3, 4, 5, 6, 7, 8], [1, 1, 1, 1, 3, 2, 3], 3), False)
    
    # @unittest.skip("")
    def test_save_divisible(self):
        self.assertEqual(save_divisible([10, 12, 13, 30, 50], 5), [10, 30, 50])


class TestStr(unittest.TestCase):
    # @unittest.skip("")
    def test_reverse_str(self):
        self.assertEqual(reverse_str("hello"), "olleh")

    # @unittest.skip("")
    def test_remove_first_n_chars(self):
        self.assertEqual(remove_first_n_chars("hello", 3), "lo")
        self.assertEqual(remove_first_n_chars("hello", 6), "")
        self.assertEqual(remove_first_n_chars("hello", 0), "")
        self.assertRaises(TypeError, remove_first_n_chars, "hello", -1)
        self.assertRaises(TypeError, remove_first_n_chars, "hello", "123")
        self.assertRaises(TypeError, remove_first_n_chars, "hello", True)
    

if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(TestMultiplicationOrSum('test_less_thousand'))
    # suite.addTest(TestMultiplicationOrSum('test_more_thousand'))

    # # 创建测试运行器
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    unittest.main()
