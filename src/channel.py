import json
import os
from googleapiclient.discovery import build


class Channel:
    api_key: str = os.getenv('API_KEY')  # API_KEY скопирован из гугла
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

    def __repr__(self) -> str:
        """Метод возвращает информацию о экземпляре класса для разработчика"""
        return f'Youtube-канал: {self.title}, id: {self.__channel_id}, подписчиков: {self.subscribers}'

    def __str__(self) -> str:
        """Метод возвращает информацию о экземпляре класса для пользователей"""
        return f'Youtube-канал: {self.title}, подписчиков: {self.subscribers}'

    def __add__(self, other) -> int:
        """Метод скадывает каналы по кол-ву количество подписчиков"""
        if isinstance(other, Channel):
            return int(self.subscribers) + int(other.subscribers)
        else:
            raise ValueError('Неправильный формат')

    def __lt__(self, other) -> int:
        """Метод сравнивает каналы по количеству подписчиков"""
        if isinstance(other, Channel):
            return self.subscribers > other.subscribers
        else:
            raise ValueError('Неправильный формат')

    def __len__(self) -> int:
        """Метод возвращает количество подписчиков канала"""
        return int(self.subscribers)

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

    @channel_id.setter
    def channel_id(self, value):
        self.__channel_id = value