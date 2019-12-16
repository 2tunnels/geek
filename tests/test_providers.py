from geek.providers import MarvelProvider


def test_marvel_provider():
    characters = MarvelProvider().get_characters()

    assert len(characters) == 1492
