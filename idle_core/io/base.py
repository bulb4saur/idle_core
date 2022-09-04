from abc import ABC, abstractmethod
from typing import Optional

from idle_core.models.player import Player


class BaseIO(ABC):
    @abstractmethod
    def save_game(self, player: Player) -> None:
        ...

    @abstractmethod
    def load_game(self, saved_game_id: str) -> Optional[Player]:
        ...
