from pydantic import BaseModel


class BaseStats(BaseModel):
    level: int = 0
    strength: int = 10
    agility: int = 10
    dexterity: int = 10
    energy: int = 10
    maximum_health: int = 100
    maximum_mana: int = 100
    current_health: int = 100
    current_mana: int = 100


class PlayerCurrencyInventory(BaseModel):
    golden_coins: int = 0
    silver_coins: int = 0


class Player(BaseModel):
    id: str
    stats: BaseStats
    currency_inventory: PlayerCurrencyInventory
