from typing import Type

from .types import Ingredient


class ParseError(Exception):
    def __init__(
        self,
        type_: Type[Ingredient],
    ) -> None:

        super().__init__(
            f"Failed to match {type_.__name__}-like object from "
            f"string using RegEx"
        )
