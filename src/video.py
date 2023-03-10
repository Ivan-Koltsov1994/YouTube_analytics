import os
from googleapiclient.discovery import build


class Video:
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

    def __init__(self, video_id: str, playlist_id: str):  # переопределяем метод базового класса
        super().__init__(video_id)
        self.__playlist_id = playlist_id  # id плэйлиста
        self.__video_id = video_id  # id видео
        self.playlist = self.youtube.playlists().list(id=playlist_id,
                                                      part='snippet,contentDetails,status').execute()  # данные о
        # плэйлисте
        self.playlist_info = self.youtube.playlistItems().list(playlistId=playlist_id,
                                                               part='snippet,contentDetails,status').execute()  #
        # полные данные  о плэйлисте
        self.title_video = self.video['items'][0]['snippet']['title']  # название видео
        self.view_count = self.video['items'][0]['statistics']['viewCount']  # количество просмотров
        self.likes_count = self.video['items'][0]['statistics']['likeCount']  # количество лайков
        self.title_playlist = self.playlist['items'][0]['snippet']['title']

    def __str__(self):
        return f'{self.title_video} ({self.title_playlist})'

    def __repr__(self):
        return f'Название видео: {self.title_video} \nПлэйлист:{self.title_playlist} '
