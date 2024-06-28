import requests
from urllib.parse import urlencode

from config import YANDEX_BASE_URL, headers


def get_yandex_url(public_key: str) -> str:
    base_url = YANDEX_BASE_URL
    final_url = base_url + urlencode(dict(public_key=public_key))
    response = requests.get(final_url)
    download_url = response.json()['href']
    return download_url


class YandexDownloader:
    def __init__(self, public_key: str):
        self.url = get_yandex_url(public_key)

    def get_bytes(self) -> bytes:
        """
        Return bytes of the file from yandex disk
        :return: bytes
        """
        response = requests.get(url=self.url, headers=headers, verify=False)
        return response.content

