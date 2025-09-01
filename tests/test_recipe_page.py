import allure

import data
from pages.recipe_page import RecipePage

from conftest import driver


class TestRecipePage():

    @allure.title('Создание рецепта')
    @allure.description('Проверить, отображается ли карточка созданного рецепта')
    @allure.testcase('Тест-кейс из Sprint_9')
    def test_create_recipe_card_recipe(self, driver):
        testcreaterecipe = RecipePage(driver)
        testcreaterecipe.go_to_url(data.BASE_URL)

        account_param = testcreaterecipe.create_account()

        testcreaterecipe.login_account(account_param[3], account_param[4])

        recipe_params = testcreaterecipe.create_recipe()

        assert recipe_params[1] == data.RECIPE_FORM_EDIT

    @allure.title('Создание рецепта')
    @allure.description('Проверить, отображается ли название, которое заполняли при создании.')
    @allure.testcase('Тест-кейс из Sprint_9')
    def test_create_recipe_name_recipe(self, driver):
        testcreaterecipe = RecipePage(driver)
        testcreaterecipe.go_to_url(data.BASE_URL)

        account_param = testcreaterecipe.create_account()

        testcreaterecipe.login_account(account_param[3], account_param[4])

        recipe_params = testcreaterecipe.create_recipe()

        assert recipe_params[0] == data.RECIPE_NAME
