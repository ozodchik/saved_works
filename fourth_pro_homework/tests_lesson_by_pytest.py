import pytest

from fourth_pro_homework.tests_theme_lesson import multiplication_str as m_s, multiplication_int as m_i


class TestExample:

    def setup(self):
        #  create user
        print("method setup")

    def teardown(self):
        # delete user
        print("method teardown")

    def test_1_numbers_3_4(self):
        print("test_numbers_3_4")
        assert m_i(5, 10) == 50 # это значит assert m_i(5, 10) == 55

    def test_2_str(self):
        print("test_str")
        assert m_s("hello", 3) == "hellohellohello"




