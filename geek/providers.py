import json
from pathlib import Path
from random import Random
from typing import Union, Optional

from .utils import normalize_name

generator_or_seed = Union[Path, int]


class Provider:
    def __init__(self, x: Optional[generator_or_seed] = None):
        if isinstance(x, Random):
            self._random = x
        else:
            self._random = Random(x)

    @property
    def characters(self):
        raise NotImplementedError

    def get_random_character(self) -> str:
        raise NotImplementedError


class MarvelProvider(Provider):
    """Characters were taken from https://www.marvel.com/comics/characters"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._load_characters()

    @property
    def characters(self):
        return self._characters

    def get_random_character(self) -> str:
        return self._random.choice(self._characters)

    def _load_characters(self):
        path = Path(__file__).parent / 'characters' / 'marvel.txt'

        with open(path, mode='r', encoding='utf-8') as f:
            self._characters = sorted({normalize_name(line.strip()) for line in f})


class DCProvider(Provider):
    """Characters were taken from https://www.dccomics.com/characters"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._load_characters()

    @property
    def characters(self):
        return self._characters

    def get_random_character(self) -> str:
        return self._random.choice(self._characters)

    def _load_characters(self):
        self._characters = sorted({normalize_name(character['name']) for character in self._read_json()})

    @staticmethod
    def _read_json():
        path = Path(__file__).parent / 'characters' / 'dc.json'

        with open(path, mode='r', encoding='utf-8') as f:
            return json.loads(f.read())
