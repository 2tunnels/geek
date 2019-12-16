from geek.generators import Generator
from geek.providers import MarvelProvider


class TestGenerator:
    def test_get_random_character(self):
        generator = Generator(1)
        generator.add_provider(MarvelProvider)

        assert generator.get_random_character() == 'venus-dee-milo'
