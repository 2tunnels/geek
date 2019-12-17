from .generators import Generator
from .providers import MarvelProvider, DCProvider


def run():
    generator = Generator()
    generator.add_provider(MarvelProvider)
    generator.add_provider(DCProvider)

    print(generator.get_random_name())
