from src.channel import Channel
from src.video import Video,PLVideo

def main():
    # channel_vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')  # id канала Вдудь
    # channel_news = Channel('UC1eFXmJNkjITxPFWTy6RsWg')  # id канала Редакции
    # channel_vdud .print_info() # информация о канале

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

    video1 = Video('9lO06Zxhu88')
    print(video1)

    video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
    print(video2.__repr__())

if __name__ == '__main__':
    main()
