import structlog
from idle_core.io import BasicFileIO
from idle_core.models import BaseStats, Player, PlayerCurrencyInventory

logger = structlog.get_logger()


class World:
    # should we check or set something on init?
    def __init__(self, player_id: str):
        # generate_player_id
        self._player_id = player_id
        self._io = BasicFileIO()

    def update_player(self, player: Player) -> None:
        player.currency_inventory.golden_coins += 1

    def load_player(self) -> Player:
        # Load current save file, if not existant, init new one
        loaded_player = self._io.load_game(saved_game_id=self._player_id)

        if not loaded_player:
            logger.debug("loading new player")
            new_player = Player(id=self._player_id, stats=BaseStats(), currency_inventory=PlayerCurrencyInventory())
            return new_player

        return loaded_player

    def save_player(self, player: Player) -> None:
        self._io.save_game(player=player)
