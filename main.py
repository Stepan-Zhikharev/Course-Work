import os
import Yandex
import VK

def upload_photos(token_vk, id_vk, token_yandex, name_folder):
    user_yandex = Yandex.Yandexdisk(token_yandex, name_folder)
    user_vk = VK.VKapi(token_vk, id_vk)
    user_vk.get_max_sizes_photos(name_folder)
    for photo in os.listdir(f'./{name_folder}'):
        x = f'{name_folder}/{photo}'
        user_yandex.upload(x, photo)






