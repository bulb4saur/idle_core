import json
import os
from typing import Optional

from idle_core.io.base import BaseIO
from idle_core.models.player import Player


class BasicFileIO(BaseIO):
    _game_save_location = "saved_games"

    # Check if directory exists, if not, crete it.
    def __init__(self) -> None:
        does_exist = os.path.exists(self._game_save_location)
        if not does_exist:
            os.mkdir(self._game_save_location)

    def save_game(self, player: Player) -> None:
        with open(f"{self._game_save_location}/{player.id}.json", "w+", encoding="utf-8") as out_file:
            out_file.write(json.dumps(player.dict(), indent=2))

    def load_game(self, saved_game_id: str) -> Optional[Player]:
        try:
            with open(f"{self._game_save_location}/{saved_game_id}.json", "r+", encoding="utf-8") as in_file:
                return Player(**json.loads(in_file.read()))
        except FileNotFoundError:
            return None
