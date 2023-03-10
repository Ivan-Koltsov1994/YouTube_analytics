def test_video_str(video):
    """Тестируем метод __str__"""
    assert video.__str__() == "Как устроена IT-столица мира / Russian Silicon Valley (English subs)"


def test_video_repr(video):
    """Тестируем метод __repr__"""
    assert video.__repr__() == "Название видео: Как устроена IT-столица мира / Russian Silicon Valley (English subs)"


def test_pcl_video_str(pcl_video):
    """Тестируем метод __str__"""
    assert pcl_video.__str__() == "Пушкин: наше все? (Литература)"


def test_pcl_video_repr(pcl_video):
    """Тестируем метод __repr__"""
    assert pcl_video.__repr__() == "Название видео: Пушкин: наше все? \nПлэйлист:Литература "
