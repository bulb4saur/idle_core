import uuid
from time import sleep

import structlog

from idle_core.world.world import World

logger = structlog.get_logger()
# get player id
PLAYER_ID = str(uuid.UUID(int=uuid.getnode()))

# we need to init and load world only once
world = World(player_id=PLAYER_ID)
player = world.load_player()

while True:
    logger.info(f"Current gold coins: {player.currency_inventory.golden_coins}")

    # update player every tic
    world.update_player(player)

    # implement "tic" system (1 second)
    # Save game every "tic"?
    world.save_player(player)
    sleep(1)
