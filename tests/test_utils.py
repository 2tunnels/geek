from geek.utils import normalize_name


def test_normalize_name():
    assert normalize_name('Spider-Man (1602)') == 'spider-man'
    assert normalize_name('Araña') == 'arana'
