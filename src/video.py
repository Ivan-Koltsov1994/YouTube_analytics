import datetime
import os

import isodate as isodate
from googleapiclient.discovery import build


class Video:
    """Класс выводящий информацию о видео по id"""

    api_key: str = os.getenv('API_KEY')  # API_KEY скопирован из гугла
    youtube = build('youtube', 'v3', developerKey=api_key)  # специальный объект для работы с API

    def __init__(self, video_id: str):  # переопределяем метод базового класса
        self.__video_id = video_id  # id видео
        self.video = self.youtube.videos().list(id=video_id,
                                                part='snippet,statistics').execute()  # данные о видео
        self.title = self.video['items'][0]['snippet']['title']  # название видео
        self.view_count = self.video['items'][0]['statistics']['viewCount']  # количество просмотров
        self.likes_count = self.video['items'][0]['statistics']['likeCount']  # количество лайков

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):
        return f'Название видео: {self.title}'


class PLVideo(Video):
    """Класс выводящий информацию о видео, входящем в плэйлист по их id"""

    def __init__(self, video_id: str, playlist_id: str):  # переопределяем метод базового класса
        super().__init__(video_id)
        self.__playlist_id = playlist_id  # id плэйлиста
        self.__video_id = video_id  # id видео
        self.playlist = self.youtube.playlists().list(id=playlist_id,
                                                      part='snippet,contentDetails,status').execute()  # данные о
        # плэйлисте
        self.playlist_info = self.youtube.playlistItems().list(playlistId=playlist_id,
                                                               part='snippet,contentDetails,status').execute()  #
        # полные данные о плэйлисте
        self.title_video = self.video['items'][0]['snippet']['title']  # название видео
        self.view_count = self.video['items'][0]['statistics']['viewCount']  # количество просмотров
        self.likes_count = self.video['items'][0]['statistics']['likeCount']  # количество лайков
        self.title_playlist = self.playlist['items'][0]['snippet']['title']  # название плэйлиста

    def __str__(self):
        return f'{self.title_video} ({self.title_playlist})'

    def __repr__(self):
        return f'Название видео: {self.title_video} \nПлэйлист:{self.title_playlist} '


class PlayList(Video):
    """ Класс выводящий информацию о плэйлисте по id"""

    def __init__(self, playlist_id: str):
        self.video_response = None
        self.video_list = None
        self.__playlist_id = playlist_id  # id плэйлиста
        self.playlist = self.youtube.playlists().list(id=playlist_id,
                                                      part='snippet,contentDetails,status').execute()  # данные о
        # плэйлисте
        self.playlist_info = self.youtube.playlistItems().list(playlistId=playlist_id,
                                                               part='snippet,contentDetails,status').execute()  #
        # полные данные о плэйлисте
        self.title_playlist = self.playlist['items'][0]['snippet']['title']  # название плэйлиста
        self.playlist_url = f"https://www.youtube.com/playlist?list={self.playlist['items'][0]['id']}"  # ссылка на
        # плэйлист

        self.video_list: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_info['items']]
        # получить все id видеороликов из плейлиста

        self.video_response = self.youtube.videos().list(part='contentDetails,statistics', id=','.join(
            self.video_list)).execute()  # Список с данными о видео в плэйлисте видео

    def __str__(self):
        return f'{self.title_playlist}'

    def __repr__(self):
        return f'Плэйлист:{self.title_playlist}. Ссылка: {self.playlist_url}'

    @property
    def total_duration(self) -> datetime:
        """Метод возвращает длительность всего плэйлиста"""

        total_duration = datetime.timedelta()  # Создаем счетчик длительности видео

        # Складываем времена всех видео в плэйлисте
        for video in self.video_response['items']:
            # Длительность видео представлены в ISO 8601 формате
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration
        # Возвращаем суммарную длительность видео
        return total_duration

    def show_best_video(self) -> str:
        """Метод возвращает длительность самого популярного видео"""

        max_likes = 0
        video_max_like = None

        for video in range(len(self.video_list)):
            like = int(self.video_response['items'][video]['statistics']['likeCount'])  # Количество лайков
            video = self.video_list[video]  # Cсылка на видео
            if like > max_likes:
                max_likes = like
                video_max_like = video
        print(f"https://youtu.be/{video_max_like}. Количество лайков:{max_likes}")
        return str(f"https://youtu.be/{video_max_like}")
