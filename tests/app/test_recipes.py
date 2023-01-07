from mixoni.app import recipes
from mixoni.types import Cocktail, Ingredient


def test_get_candidate_cocktails() -> None:

    # GIVEN
    DUMMY_INGREDIENTS = {
        Ingredient.GIN,
        Ingredient.CAMPARI,
        Ingredient.RED_VERMOUTH,
        Ingredient.WHITE_VERMOUTH,
        Ingredient.SODA_WATER,
    }
    expected = {
        Cocktail.NEGRONI,
        Cocktail.MARTINI,
        Cocktail.CAMPARI_SODA,
    }

    # WHEN
    actual = recipes.get_candidate_cocktails(DUMMY_INGREDIENTS)

    # THEN
    assert actual == expected
