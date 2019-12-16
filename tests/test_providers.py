from geek.providers import MarvelProvider


def test_marvel_provider():
    provider = MarvelProvider(1)

    assert len(provider.characters) == 1251
    assert provider.get_random_character() == 'doctor-strange'
