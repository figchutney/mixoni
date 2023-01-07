from typing import Any

from flask import render_template, request

from ..app import app
from ..types import Ingredient
from .recipes import RECIPES, get_candidate_cocktails
from .utils import convert_string_to_ingredient


@app.route("/", methods=["POST", "GET"])
def root() -> Any:

    print(request.form.getlist("ingredient"))
    if request.form.get("ingredient") is not None:
        print("yay")
        ingredients = {
            convert_string_to_ingredient(i)
            for i in request.form.getlist("ingredient")
        }
        candidates = get_candidate_cocktails(ingredients)
        return render_template(
            "root.html",
            ingredients=list(Ingredient),
            cocktails={c: i for c, i in RECIPES.items() if c in candidates},
        )
    print("uhoh")
    return render_template("root.html", ingredients=list(Ingredient))
