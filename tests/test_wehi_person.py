from rdm_models.core.wehi_person import WehiPerson
from rdm_models.core.consts import WEHI_ROR_ID


def test_wehi_person_creation():
    person = WehiPerson(
        given_name="John", family_name="Doe", email="john.doe@example.com"
    )

    assert person.given_name == "John"
    assert person.family_name == "Doe"
    assert person.email == "john.doe@example.com"
    assert person.ror_id == WEHI_ROR_ID
