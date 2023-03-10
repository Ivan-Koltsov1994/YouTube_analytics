import pytest
from src.channel import Channel
from src.video import Video,PLVideo

@pytest.fixture()
def channel1():
    return Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')

@pytest.fixture()
def channel2():
    return Channel('UC1eFXmJNkjITxPFWTy6RsWg')

@pytest.fixture()
def video():
    return Video("9lO06Zxhu88")

@pytest.fixture()
def pcl_video():
    return PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')