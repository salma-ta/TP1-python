import logging

log = logging.getLogger(__name__)


class CharacterError(Exception):
    """Base class for Character error"""


class Character:
    """To implement"""
def __init__(self, _name: str,_life:float,_attack:float,_defense:float):
        self._name = name
        self._life = _life
        self._attack = _attack
        self._defense = _defense
def take_damages(damage_value: float):
     damage=damage_value*(1-self._defense)
     self._life=self._life-damage

def _rep_(self):
        return f"Character({self._name},{self._life})"
@property
def name(self):
     return self._name
@property
def is_dead(self):
     if self._life>0:
          return True
     else:
          return false
class Weapon:
    """To implement"""
def __init__(self, name: str,attack:float):
        self._name = name
        self.attack= attack

class Warrior:
    """To implement"""


class Magician:
    """To implement"""
