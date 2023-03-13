from src.channel import Channel
from src.video import Video, PLVideo, PlayList


def main():
    # channel_vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')  # id канала Вдудь
    # channel_news = Channel('UC1eFXmJNkjITxPFWTy6RsWg')  # id канала Редакции
    # channel_vdud .print_info() # информация о канале
    # print(channel_vdud.__add__(channel_news))
    # print(channel_vdud.title)
    # print(channel_vdud.video_count)
    # print(channel_vdud.url)
    # channel_vdud.channel_id = 'new_id'
    # print(Channel.get_service())
    # channel_vdud.record_to_json('vdud.json')
    # channel_vdud.print_info()

    # print(channel_vdud)
    # print(channel_news)

    # print(channel_vdud > channel_news)
    # print(channel_vdud < channel_news)
    # print(channel_vdud + channel_news)

    # video1 = Video('9lO06Zxhu88')
    # print(video1)

    # video2 = PLVideo('BBotskuyw_M', 'PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
    # print(video2.__repr__())

    pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
    print(pl.title_playlist)
    print(pl.playlist_url)

    duration = pl.total_duration
    print(duration)

    print(type(duration))
    print(duration.total_seconds())

    pl.show_best_video()


if __name__ == '__main__':
    main()
