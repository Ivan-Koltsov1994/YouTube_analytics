def test_str(channel1):
    """Тестируем метод __str__"""
    assert channel1.__str__() == "Youtube-канал: вДудь, подписчиков: 10300000"


def test_lt(channel1, channel2):
    """Тестируем метод __it__"""
    assert channel1.__lt__(channel2) is False


def test_add(channel1, channel2):
    """Тестируем метод __add__"""
    assert channel1.__add__(channel2) == 14000000


def test_len(channel1):
    """Тестируем метод __len__"""
    assert channel1.__len__() == 10300000


def test_repr(channel1):
    """Тестируем метод __repr__"""
    assert channel1.__repr__() == 'Youtube-канал: вДудь, id: UCMCgOm8GZkHp8zJ6l7_hIuA, подписчиков: 10300000'


def test_record_to_json(channel1):
    """Тестируем, что метод __record_to_json__ правильно записывает данные в json- формате"""
    channel1.record_to_json('v.json')
    assert open('v.json', 'r') is not None


def test_get_service(channel1):
    """Тестируем, что при выполнении метода получаем объект для работы с API вне класса"""
    assert channel1.get_service() is not None


def test_channel_id(channel1):
    """Тестируем, что метод channel_id.setter дает записывать данные в экземпляр класса"""
    channel1.channel_id = "12345"
    assert channel1.channel_id == "12345"
