import allure


from faker import Faker
fake = Faker("ru_RU")

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    @allure.step('ожидание текста войти на сайт на главной странице')
    def get_text_from_main_page(self):
        self.wait_to_element(MainPageLocators.main_page_text)
        return self.get_text_from_element(MainPageLocators.main_page_text)

    @allure.step('получение текста на кнопке войти')
    def get_text_from_login_button_on_main_page(self):
        self.wait_to_element(MainPageLocators.click_login_button)
        return self.get_text_from_element(MainPageLocators.click_login_button)

    @allure.step('получение тескта на кнопке выход')
    def get_text_from_logaut_button(self):
        self.wait_to_element(MainPageLocators.click_logout_button)
        return self.get_text_from_element(MainPageLocators.click_logout_button)

    @allure.step('получение тескта рецепты')
    def get_text_from_recipes_text(self):
        self.wait_to_element(MainPageLocators.main_page_recipes_text)
        return self.get_text_from_element(MainPageLocators.main_page_recipes_text)

