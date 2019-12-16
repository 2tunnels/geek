import pytest

from geek.generators import Generator
from geek.providers import MarvelProvider


class TestGenerator:
    def test_no_provider_added(self):
        generator = Generator(1)

        with pytest.raises(RuntimeError) as excinfo:
            generator.get_random_character()

        assert str(excinfo.value) == 'No provider added'

    def test_get_random_character(self):
        generator = Generator(1)
        generator.add_provider(MarvelProvider)

        assert generator.get_random_character() == 'venus-dee-milo'
