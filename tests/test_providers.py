from random import Random

from geek.providers import MarvelProvider


class TestMarvelProvider:
    def test_generator(self):
        provider = MarvelProvider(Random(1))

        assert len(provider.characters) == 1251
        assert provider.get_random_character() == 'doctor-strange'

    def test_seed(self):
        provider = MarvelProvider(1)

        assert len(provider.characters) == 1251
        assert provider.get_random_character() == 'doctor-strange'
