import requests
import json


class YandexResources:
    def __init__(self, token: str):
        self.token = token
        self.base_url = "https://cloud-api.yandex.net/v1/disk/resources"

    def create_file(self, file_path):
        HEADERS = {"Authorization": f"OAuth {self.token}"}
        response = requests.put(self.base_url,
                                headers=HEADERS,
                                params={
                                    "path": file_path
                                })
        status_code_for_test = response.status_code
        if status_code_for_test == "201" or status_code_for_test == "200":
            print("OK")
            return status_code_for_test
        else:
            print("error")
            return status_code_for_test



