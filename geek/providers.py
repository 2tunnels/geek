from pathlib import Path


class BaseProvider:
    def get_characters(self) -> set:
        raise NotImplementedError


class MarvelProvider(BaseProvider):
    """Characters were taken from https://www.marvel.com/comics/characters"""

    def get_characters(self) -> set:
        path = Path(__file__).parent / 'characters' / 'marvel.txt'

        with open(path, mode='r', encoding='utf-8') as f:
            # TODO: Normalize character name.
            characters = {line.strip() for line in f}

        return characters
