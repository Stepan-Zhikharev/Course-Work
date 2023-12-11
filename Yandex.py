import requests
class Yandexdisk:
    def __init__(self, token, name_folder):
        self.name_folder = name_folder
        self.token = token
    def common_headers(self):
        return  {'Authorization': f'OAuth {self.token}'}
    def create_folder(self, name_folder):
        params = {'path': name_folder}
        requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                     params=params,
                     headers=self.common_headers())
        return name_folder
    def url_for_upload(self, name_image):
        params = {'path': f'{self.create_folder(self.name_folder)}/{name_image}'}
        url = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                           params=params,
                           headers=self.common_headers())
        url_upload = url.json().get('href', '')
        return url_upload
    def upload(self, image, name_image):
        with open(image, 'rb') as f:
            requests.put(self.url_for_upload(name_image=name_image), files={"file": f})