from pydantic import BaseModel, EmailStr
from typing import Literal

from rdm_models.core.consts import WEHI_ROR_ID


class WehiPerson(BaseModel):
    given_name: str
    family_name: str
    email: EmailStr
    # Literal[] does not support variables so repetition is unavoidable
    affiliation: Literal["https://ror.org/01b6kha49"] = WEHI_ROR_ID
