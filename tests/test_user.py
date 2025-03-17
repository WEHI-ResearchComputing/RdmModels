from rdm_models import Dummy


def test_dummy():
    d = Dummy(id=1, name="Foo")
    assert d.id == 1
    assert d.name == "Foo"
    assert d.age is None
