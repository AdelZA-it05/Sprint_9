import allure

import data
from pages.recipe_page import RecipePage


class TestRecipePage():

    @allure.title('Создание рецепта')
    @allure.description('Проверить, отображается ли карточка созданного рецепта')
    @allure.testcase('Тест-кейс из Sprint_9')
    def test_create_recipe_card_recipe(self, driver, createaccount, loginaccount):
        testcreaterecipe = RecipePage(driver)

        recipe_params = testcreaterecipe.create_recipe()

        assert recipe_params[1] == data.RECIPE_FORM_EDIT

    @allure.title('Создание рецепта')
    @allure.description('Проверить, отображается ли название, которое заполняли при создании.')
    @allure.testcase('Тест-кейс из Sprint_9')
    def test_create_recipe_name_recipe(self, driver, createaccount, loginaccount):
        testcreaterecipe = RecipePage(driver)

        recipe_params = testcreaterecipe.create_recipe()

        assert recipe_params[0] == data.RECIPE_NAME
