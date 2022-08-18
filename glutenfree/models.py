from glutenfree import db


class Recipe(db.Model):
    # schema for Recipes
    id = db.column(db.integer, primary_key=True)
    recipe_name = db.Column(db.Text, unique=True, nullable=False)
    recipe_description = db.Column(db.Text, nullable=False)
    recipe_ingrediants = db.Column(db.Text, nullable=False)
    recipe_method = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return self.recipe_name
        return self.recipe_description
        return self.recipe_ingrediants
        return self.recipe_method
        