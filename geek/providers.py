from pathlib import Path

from .utils import normalize_name


class BaseProvider:
    def get_characters(self) -> set:
        raise NotImplementedError


class MarvelProvider(BaseProvider):
    """Characters were taken from https://www.marvel.com/comics/characters"""

    def get_characters(self) -> set:
        path = Path(__file__).parent / 'characters' / 'marvel.txt'

        with open(path, mode='r', encoding='utf-8') as f:
            characters = {normalize_name(line.strip()) for line in f}

        return characters
