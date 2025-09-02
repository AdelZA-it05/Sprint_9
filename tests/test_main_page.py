import time

import allure

import data
from pages.main_page import MainPage


class TestMainPage():

    @allure.title('Создание аккаунта')
    @allure.description('Проверка произошёл ли переход на страницу авторизации.')
    @allure.testcase('Тест-кейс из Sprint_9')
    def test_create_account_autorization_page(self, driver):
        testclickaccount = MainPage(driver)
        testclickaccount.go_to_url(data.BASE_URL)

        testclickaccount.create_account()

        assert testclickaccount.get_text_from_main_page() == data.TEXT_ON_MAIN_PAGE

    @allure.title('Создание аккаунта')
    @allure.description('Проверка отображается ли форма авторизации.')
    @allure.testcase('Тест-кейс из Sprint_9')
    def test_create_account_autorization_form(self, driver):
        testclickaccount = MainPage(driver)
        testclickaccount.go_to_url(data.BASE_URL)

        testclickaccount.create_account()

        assert testclickaccount.get_text_from_login_button_on_main_page() == data.TEXT_ON_LOGIN_BUTTON


    @allure.title('Авторизация')
    @allure.description('Проверка произошёл ли переход на главную страницу.')
    @allure.testcase('Тест-кейс из Sprint_9')
    def test_login_account_main_page(self, driver, createaccount):
        testloginaccount = MainPage(driver)

        testloginaccount.login_account(createaccount[3], createaccount[4])

        assert testloginaccount.get_text_from_recipes_text() == data.TEXT_RECIPES

    @allure.title('Авторизация')
    @allure.description('Проверка отображается ли кнопка «Выход».')
    @allure.testcase('Тест-кейс из Sprint_9')
    def test_login_account_logout_button(self, driver, createaccount):
        testloginaccount = MainPage(driver)

        testloginaccount.login_account(createaccount[3], createaccount[4])

        assert testloginaccount.get_text_from_logaut_button() == data.TEXT_ON_LOGAUT_BUTTON
