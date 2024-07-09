from typing import List

from fastapi import FastAPI
from sqlalchemy import select, desc, asc

from .database import engine, session
from . import models
from . import schemas

app = FastAPI()


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await session.close()
    await engine.dispose()


@app.post('/recipes/', response_model=schemas.DetailedReviewRecipe)
async def recipes(recipe: schemas.RecipeIn) -> models.Recipe:
    """
    Creating a new recipe
    """
    new_recipe = models.Recipe(**recipe.model_dump())
    session.add(new_recipe)
    await session.commit()
    return new_recipe


@app.get('/recipes/{recipe_id}', response_model=schemas.DetailedReviewRecipe)
async def get_recipe(recipe_id: int) -> models.Recipe:
    """
    Receiving detailed information about the recipe with the given id
    """
    recipe = await session.get(models.Recipe, recipe_id)
    if recipe:
        recipe.views = recipe.views + 1
        await session.commit()
    return recipe


@app.get('/recipes/', response_model=List[schemas.GeneralReviewRecipes])
async def get_recipes() -> List[models.Recipe]:
    """
    Receiving all recipes in sorted form (by number of views and cooking time)
    """
    res = await session.execute(
        select(models.Recipe).order_by(desc(models.Recipe.views), asc(models.Recipe.cooking_time))
    )
    return res.scalars().all()
