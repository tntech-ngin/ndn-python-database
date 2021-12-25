#    @Author: Justin C Presley
#    @Author-Email: justincpresley@gmail.com
#    @Project: NDN Storage
#    @Source-Code: https://github.com/justincpresley/ndn-python-storage
#    @Pip-Library: https://pypi.org/project/ndn-storage

from abc import ABC, abstractmethod
from ndn.name_tree import NameTrie
from typing import Optional
from time import time as get_time

class Storage(ABC):
    def __init__(self) -> None:
        cache:NameTrie = NameTrie()
    @staticmethod
    def _time_ms() -> int:
        return int(get_time() * 1000)
    @abstractmethod
    def put_packet(self, name:NonStrictName, packet:bytes) -> None:
        return
    @abstractmethod
    def get_packet(self, name:NonStrictName, can_be_prefix:bool=False, must_be_fresh:bool=False) -> Optional[bytes]:
        return
    @abstractmethod
    def remove_packet(self, name:NonStrictName) -> bool:
        return