from pydantic import BaseModel


class BaseRecipe(BaseModel):
    """
    Base recipe model
    """
    name: str
    cooking_time: int


class GeneralReviewRecipes(BaseRecipe):
    """
    Represents a recipe in a general table with a list of all recipes
    """
    views: int

    class Config:
        orm_mode = True


class DetailedReviewRecipe(BaseRecipe):
    """
    Represents a recipe when displaying detailed information,
    and also as a response to creating a new recipe
    """

    ingredients: str
    description: str

    class Config:
        orm_mode = True


class RecipeIn(BaseRecipe):
    """
    Scheme for creating a recipe
    """
    ingredients: str
    description: str
