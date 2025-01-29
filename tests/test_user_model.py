from src import UserModel


def test_user_model():
    user = UserModel(id=1, name="Foo")
    assert user.id == 1
    assert user.name == "Foo"
    assert user.age is None
