import json
import os

from googleapiclient.discovery import build


class Channel:
    api_key: str = os.getenv('API KEY')  # API_KEY скопирован из гугла
    youtube = build('youtube', 'v3', developerKey=api_key)  # специальный объект для работы с API

    def __init__(self, channel_id):
        self.channel_id = channel_id
        self.channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

    def print_info(self):
        """Метод возвращает общую информацию о YouTube канале"""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))
