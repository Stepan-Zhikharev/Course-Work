import json
import os.path
import requests
class VKapi:
    base_url = 'https://api.vk.com/method'
    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id
    def common_params(self):
        return {'access_token': self.token,
                'v': '5.199'}
    def get_list_photos(self):
        params = self.common_params()
        params.update({'owner_id': self.user_id,
                       'album_id': 'profile',
                       'extended': '1'})
        response = requests.get(f'{self.base_url}/photos.get', params=params)
        if 200 <= response.status_code < 300:
            return response.json()
    def get_max_sizes_photos(self, name_folder):
        max_size_photos = {}
        info_photos = []
        list_photos = self.get_list_photos().get('response', '').get('items')
        for photos in list_photos:
            max_size = max(photos.get('sizes'), key=(lambda x: x.get('height'))).get('url')
            name_photos = f"{photos.get('likes').get('count')}.jpg"
            max_size_photos.update({name_photos: max_size})
            size = max(photos.get('sizes'), key=(lambda x: x.get('height'))).get('type')
            info = {'file_name': name_photos, 'size': size}
            info_photos.append(info)
        with open('photo_info.json', 'w') as file:
            json.dump(info_photos, file, indent=2)
        for photo, url in max_size_photos.items():
            download_photo = requests.get(url)
            if not os.path.exists(name_folder):
                os.mkdir(name_folder)
            with open(f'{name_folder}/{photo}', 'wb') as file:
                file.write(download_photo.content)