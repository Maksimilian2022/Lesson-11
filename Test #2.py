import requests

TOKEN = 'AQAAAABR6sW2AADLW-hiYhDRWkXIgVyXB5LPvQQ'

class YaUploader:
    def __init__(self, token: str):
        self.token = TOKEN

    def get_upload_link(self, file_path):
        upload_url = 'https://disk.yandex.ru/client/disk/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
        params = {'path': file_path, 'overwrite': 'true'}
        responce = requests.get(upload_url, headers=headers, params=params)
        print(responce.json())


    def upload_file(self, disk_file_path, filename):
        upload_url = 'https://disk.yandex.ru/client/disk/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}
        responce_href = self.get_upload_link(file_path = file_path)
        url = responce_href.get('href', '')
        responce = requests.put(url, data=open(filename, 'rb'))





