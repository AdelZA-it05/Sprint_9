from selenium.webdriver.common.by import By

import allure

import pathlib

from faker import Faker
fake = Faker("ru_RU")

from pages.base_page import BasePage
from locators.recipe_page_locatros import RecipePageLocators
import data


class RecipePage(BasePage):


    @allure.step('создание рецепта')
    def create_recipe(self, recipe_name=data.RECIPE_NAME, inredient_name=data.RECIPE_INGREDIENT, ingredient_vol=data.INGREDIENT_VOL, recipe_time=data.RECIPE_TIME, recipe_descr=data.RECIPE_DESCR, recipe_photo='caprese.jpg'):
        create_recipe = self.find_element_with_wait(RecipePageLocators.click_create_recipe)
        self.wait_element_to_clickable(create_recipe)
        self.click_web_element(create_recipe)

        input_fields = self.find_elements_with_wait(RecipePageLocators.recipe_fields)

        self.add_text_to_web_element(input_fields[0], recipe_name)

        self.add_ingredients(input_fields[1], input_fields[2])

        self.add_text_to_web_element(input_fields[3], recipe_time)
        self.add_text_to_element(RecipePageLocators.recipe_text, recipe_descr)

        self.load_recipe_file()

        # создание рецепта
        self.scroll_element(RecipePageLocators.button_create_recipe)
        self.click_element_locator(RecipePageLocators.button_create_recipe)
        # ожидание открытия карточки рецепта
        self.wait_to_element(RecipePageLocators.recipe_card_name)

        return [self.get_text_from_element(RecipePageLocators.recipe_card_name), self.get_text_from_element(RecipePageLocators.recipe_card_edit)]

    @allure.step('добавление ингредиентов рецепта')
    def add_ingredients(self, web_inredient_name, web_ingredient_vol):
        # ввод ингредиента
        self.add_text_to_web_element(web_ingredient_vol, data.INGREDIENT_VOL)
        self.add_text_to_web_element(web_inredient_name, data.RECIPE_INGREDIENT)
        # выбор ингредиента из списка поиска
        parent_div = self.find_element_with_wait(RecipePageLocators.ingredients_list)
        first_child_div = parent_div.find_element(*RecipePageLocators.recipe_ingredient)
        first_child_div.click()
        # добавление ингредиента
        self.click_element_locator(RecipePageLocators.click_add_ingredient)


    @allure.step('загрузка файла')
    def load_recipe_file(self, recipe_photo='caprese.jpg'):
        # формирование пути к файлу
        APP_DIR = pathlib.Path(__file__).parent
        parent_dir = APP_DIR.parent
        image_dir = parent_dir/"assets"
        file_path = str(image_dir) + "/" + recipe_photo # "/caprese.jpg"

        # загрузка файла
        self.scroll_element(RecipePageLocators.button_create_recipe)
        file_input = self.find_element_base(RecipePageLocators.input_file)
        file_input.send_keys(file_path)
