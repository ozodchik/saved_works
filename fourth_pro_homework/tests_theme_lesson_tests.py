import unittest

from fourth_pro_homework.tests_theme_lesson import multiplication_str as m_s, multiplication_int as m_i


class TestExample(unittest.TestCase):

    def setUp(self):
        #  create user
        print("method SetUp")

    def test_1_numbers_3_4(self):
        print("test_numbers_3_4")
        self.assertEqual(m_i(3, 4), 12)  # это значит assert m_i(5, 10) == 55

    def test_2_str(self):
        print("test_str")
        self.assertEqual(m_s("hello", 3), "hellohellohello")

    def tearDown(self):
        #delete user
        print("method tearDown")
