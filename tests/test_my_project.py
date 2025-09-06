from my_project import __version__


def test_version():
    assert __version__ == "0.1.0"


def test_basic_import():
    import my_project

    assert my_project is not None
