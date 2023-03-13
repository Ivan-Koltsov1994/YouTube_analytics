def test_video_str(video):
    """Тестируем метод __str__класса Video"""
    assert video.__str__() == "Как устроена IT-столица мира / Russian Silicon Valley (English subs)"


def test_video_repr(video):
    """Тестируем метод __repr__класса Video"""
    assert video.__repr__() == "Название видео: Как устроена IT-столица мира / Russian Silicon Valley (English subs)"


def test_pcl_video_str(pcl_video):
    """Тестируем метод __str__класса PLVideo"""
    assert pcl_video.__str__() == "Пушкин: наше все? (Литература)"


def test_pcl_video_repr(pcl_video):
    """Тестируем метод __repr__класса PLVideo"""
    assert pcl_video.__repr__() == "Название видео: Пушкин: наше все? \nПлэйлист:Литература "


def test_playlist_str(playlist):
    """Тестируем метод __str__ класса Playlist"""
    assert playlist.__str__() == "Редакция. АнтиТревел"


def test_playlist_repr(playlist):
    """Тестируем метод __repr__ класса Playlist"""
    assert playlist.__repr__() == "Плэйлист:Редакция. АнтиТревел. Ссылка: " \
                                  "https://www.youtube.com/playlist?list=PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb "


def test_playlist_total_duration(playlist):
    """Тестируем, что метод total_duration возвращает верную длительность видео в плэйлисте"""
    assert str(playlist.total_duration) == "3:41:01"


def test_playlist_show_best_video(playlist):
    """Тестируем, что метод show_best_video нужную ссылку о наиболее популярном видео в плэйлисте"""
    assert playlist.show_best_video() == "https://youtu.be/9Bv2zltQKQA"
