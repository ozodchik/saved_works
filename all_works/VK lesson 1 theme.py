from urllib.parse import urljoin
from urllib.parse import urlencode

import requests
#
# ЭТО КОД ДЛЯ ПОЛУЧЕНИЕ ТОКЕНА
APP_ID = 7637207
OAUTH_URL = "https://oauth.vk.com/authorize"
REDIRECT_URI = "https://oauth.vk.com/blank.html"
SCOPE = "status"
OAUTH_PARAMS ={
    "redirect_uri": REDIRECT_URI,
    "scope": SCOPE,
    "response_type": "token",
    "client_id": APP_ID
}
print('?'.join([OAUTH_URL, urlencode(OAUTH_PARAMS)]))


TOKEN = "2dafda31476547e22664880af6ae8663bd60e1979f699d14ddb2883e7ef02b3eff2fa97d630c35490e991"
API_BASE_URL = "https://api.vk.com/method/"
V = "5.214"

#
# class APIGet:
#     BASE_URL = API_BASE_URL
#
#     def __init__(self, token=TOKEN, version=V):
#         self.token = token
#         self.version = version
#
#     def get_user_status(self):
#         status_get_url = urljoin(API_BASE_URL, "status.get")
#         res = requests.get(status_get_url, params={
#             "access_token": self.token,
#             "v": self.version
#         })
#         return res.json()
#
#     def set_user_status(self, text):
#         status_set_url = urljoin(API_BASE_URL, "status.set")
#         res = requests.get(status_set_url, params={
#             "access_token": self.token,
#             "v": self.version,
#             "text": text
#         })
#         return res.json()
#
#
# if __name__ == "__main__":
#     vkclient = APIGet(TOKEN, V)
#     print(vkclient.get_user_status())



