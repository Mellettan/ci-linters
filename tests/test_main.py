from typing import List

from src.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_recipes_1():
    response = client.get("/recipes/1")
    assert response.status_code == 200
    data = response.json()

    assert data["name"] == "potatoes"
    assert data["description"] == "text"
    assert data["cooking_time"] == 15
    assert data["ingredients"] == "potato"


def test_read_all_recipes():
    response = client.get("/recipes/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, List)


def test_create_recipe():
    new_recipe_data = {
        "name": "New Recipe",
        "description": "A tasty new recipe",
        "cooking_time": 30,
        "ingredients": "ingredient1, ingredient2"
    }

    response = client.post("/recipes/", json=new_recipe_data)

    assert response.status_code == 200

    data = response.json()
    assert data["name"] == new_recipe_data["name"]
    assert data["description"] == new_recipe_data["description"]
    assert data["cooking_time"] == new_recipe_data["cooking_time"]
    assert data["ingredients"] == new_recipe_data["ingredients"]