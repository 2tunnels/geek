from pathlib import Path
from random import Random
from typing import Union, Optional, List, Type

from .providers import Provider

generator_or_seed = Union[Path, int]


class Generator:
    def __init__(self, x: Optional[generator_or_seed] = None):
        if isinstance(x, Random):
            self._random = x
        else:
            self._random = Random(x)

        self._providers: List[Provider] = []

    def add_provider(self, provider_class: Type[Provider]):
        # noinspection PyTypeChecker
        self._providers.append(provider_class(self._random))

    def get_random_character(self) -> str:
        return self._random.choice(self._providers).get_random_character()
