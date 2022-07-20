import requests



class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def creat_folder(path):
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        URL = 'https://cloud-api.yandex.net/v1/disk/resources'
        requests.put(f'{URL}?path={path}', headers=headers)

    def upload(self, path_to_file):
        file_name = path_to_file.split('/')[-1]
        upload_url = 'https://disk.yandex.ru/client/disk/v1/disk/resources/copy'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
        params = {'from': path_to_file, 'path': file_name}
        responce = requests.post(upload_url, headers=headers, params=params)
        return responce

if __name__ == '__main__':
    path_to_file = input('Введите путь: ')
    token = input('Введите токен: ')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)



