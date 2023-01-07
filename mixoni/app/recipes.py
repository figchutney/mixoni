from ..types import Cocktail, Ingredient

RECIPES = {
    Cocktail.CAMPARI_SODA: {
        Ingredient.CAMPARI,
        Ingredient.SODA_WATER,
    },
    Cocktail.ESPRESSO_MARTINI: {
        Ingredient.VODKA,
        Ingredient.ESPRESSO,
        Ingredient.COFFEE_LIQUER,
        Ingredient.SALT,
    },
    Cocktail.JUNGLE_BIRD: {
        Ingredient.DARK_RUM,
        Ingredient.CAMPARI,
        Ingredient.LIME_JUICE,
        Ingredient.CASTER_SUGAR_SYRUP,
        Ingredient.PINAPPLE_JUICE,
    },
    Cocktail.MARTINI: {
        Ingredient.GIN,
        Ingredient.WHITE_VERMOUTH,
    },
    Cocktail.NEGRONI: {
        Ingredient.GIN,
        Ingredient.RED_VERMOUTH,
        Ingredient.CAMPARI,
    },
    Cocktail.OLD_FASHIONED: {
        Ingredient.BOURBON_WHISKY,
        Ingredient.BITTERS,
        Ingredient.MUSCAVADO_SUGAR_SYRUP,
    },
    Cocktail.WHISKY_SOUR: {
        Ingredient.BOURBON_WHISKY,
        Ingredient.LEMON_JUICE,
        Ingredient.CASTER_SUGAR_SYRUP,
        Ingredient.BITTERS,
        Ingredient.EGG_WHITE,
    },
}


def get_candidate_cocktails(ingredients: set[Ingredient]) -> set[Cocktail]:
    return {c for c, i in RECIPES.items() if i.issubset(ingredients)}
