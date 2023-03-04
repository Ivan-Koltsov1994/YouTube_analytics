import pytest
from src.Dataclass import Channel

@pytest.fixture()
def channel1():
    return Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')

@pytest.fixture()
def channel2():
    return Channel('UC1eFXmJNkjITxPFWTy6RsWg')
