import pytest
from fourth_pro_homework.unittest_yandex_API import YandexResources
class YandexTest:
    def setup(self):
        print("setup method")

    def teardown(self):
        print("method teardown")

    def test_yandex(self):
        test = YandexResources("AgAAAABHbNOAAADLW-DQyGa69El4iLm7Srf0ljI")
        assert test.create_file("/first") == "201"