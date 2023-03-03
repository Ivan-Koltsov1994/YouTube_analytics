import json
import os
from googleapiclient.discovery import build


class Channel:
    api_key: str = os.getenv('API KEY')  # API_KEY скопирован из гугла
    youtube = build('youtube', 'v3', developerKey=api_key)  # специальный объект для работы с API

    def __init__(self, channel_id: str):
        self.__channel_id = channel_id  # id канала
        self.channel = self.youtube.channels().list(id=channel_id,
                                                    part='snippet,statistics').execute()  # данные о канале
        self.title = self.channel['items'][0]['snippet']['title']  # название канала
        self.description = self.channel['items'][0]['snippet']['description']  # описание канала
        self.url = 'https://www.youtube.com/channel/' + self.__channel_id  # ссылка на канала
        self.subscribers = self.channel['items'][0]['statistics']['subscriberCount']  # количество подписчиков
        self.video_count = self.channel['items'][0]['statistics']['videoCount']  # количество видео
        self.view_count = self.channel['items'][0]['statistics']['viewCount']  # количество просмотров

    @property
    def channel_id(self):
        """Метод запрещает внесение изменений в id канала"""
        return self.__channel_id

    def print_info(self):
        """Метод возвращает общую информацию о YouTube канале"""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """Метод получает объект для работы с API вне класса"""
        return cls.youtube

    def record_to_json(self, filename):
        """метод сохраняет информацию по каналу, хранящуюся в атрибутах экземпляра класса Channel, в json-файл. """
        data = {
            'channel_id': self.__channel_id,
            'title': self.title,
            'description': self.description,
            'channel_link': self.url,
            'subscriber_count': self.subscribers,
            'video_count': self.video_count,
            'view_count': self.view_count
        }
        with open(filename, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)


#vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')

# print(vdud.title)
# print(vdud.video_count)
# print(vdud.url)
# vdud.channel_id = 'new_id'
#print(Channel.get_service())
#vdud.record_to_json('vdud.json')