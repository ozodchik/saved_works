from fourth_pro_homework.pro_test_docs_homework import id_doc as i_d, a_shelf as a_sh, doc_list as d_l, add_doc as a_d
import pytest


class TestsFunctions:

    def setup(self):
        #  create user
        print("method setup")

    def teardown(self):
        # delete user
        print("method teardown")

    def test_i_d(self):
        print(f"working testing test_i_d")
        assert i_d("11-2")

    def test_a_sh(self):
        print(f"working testing test_a_sh")
        assert a_sh("10006")

    def test_d_l(self):
        print(f"working testing test_d_l")
        assert d_l()

    def test_a_d(self):
        print(f"working testing test_a_d")
        assert a_d("passport", "2001", "ozod", "3")