import re

from ..exceptions import ParseError
from ..types import Ingredient

REGEX = {
    "ingredient": re.compile(r"(?<=Ingredient\.).+"),
}


def convert_string_to_ingredient(string: str) -> Ingredient:
    match = re.search(REGEX["ingredient"], string=string)
    if match is None:
        raise ParseError(type_=Ingredient)
    return Ingredient(match.group())
