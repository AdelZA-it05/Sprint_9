from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker
fake = Faker("ru_RU")
import allure

from locators.main_page_locators import MainPageLocators
import data


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 25
        self.wait = WebDriverWait(self.driver, self.timeout)

    @allure.step('переход по url')
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step('поиск элемента')
    def find_element_base(self, locator):
        return self.driver.find_element(*locator)
    @allure.step('поиск элемента с ожиданием')
    def find_element_with_wait(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('поиск элемента с ожиданием кликабельности')
    def find_element_with_wait_clickable(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step('поиск элементов с ожиданием')
    def find_elements_with_wait(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step('клик по элемент локатора')
    def click_element_locator(self, locator):
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('клик по локатору кнопки для Firefox')
    def click_on_element_for_firefox(self, locator):
        element = self.find_element_with_wait(locator)
        ActionChains(self.driver).move_to_element(element).click().perform()



    @allure.step('клик по web-элементу')
    def click_web_element(self, element):
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.element_to_be_clickable(element))
        element.click()


    @allure.step('клик по web-элементу кнопки для Firefox')
    def click_web_element_for_firefox(self, element):
        ActionChains(self.driver).move_to_element(element).click().perform()

    @allure.step('добавление текста на элемент')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('добавление текста на web-элемент')
    def add_text_to_web_element(self, web_element, text):
        web_element.send_keys(text)

    @allure.step('получение текста элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('получение текущего url')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('ожидание видимости элемента')
    def wait_to_element(self, element_locator):
        self.wait.until(expected_conditions.visibility_of_element_located(element_locator))

    @allure.step('ожидание кликабельности элемента')
    def wait_element_to_clickable(self, element_locator):
        self.wait.until(expected_conditions.element_to_be_clickable(element_locator))

    @allure.step('ожидание элемента по условию отсутствия/присутствия текста на элементе')
    def wait_until_condition(self, element_locator, expected_text, is_param):
        if is_param == 0:
            self.wait_to_element(element_locator, expected_text)
            self.wait.until(
                expected_conditions.text_to_be_present_in_element(element_locator, expected_text)
            )
        else:
            self.wait.until_not(
                expected_conditions.text_to_be_present_in_element(element_locator, expected_text)
            )

    @allure.step('прокрутка элемента по локатору')
    def scroll_element(self, locator):
        """Пролистать страницу до элемента"""
        element = self.find_element_with_wait(locator)
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
        except:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)


    @allure.step('перетаскивание элемента')
    def drag_and_drop_element(self, locator_from, locator_to):
        WebDriverWait(self.driver, 25).until(expected_conditions.visibility_of_element_located(locator_from))
        WebDriverWait(self.driver, 25).until(expected_conditions.visibility_of_element_located(locator_to))
        element_from = self.driver.find_element(*locator_from)
        element_to = self.driver.find_element(*locator_to)
        self.driver.execute_script("""
           var source = arguments[0];
           var target = arguments[1];
           var evt = document.createEvent("DragEvent");
           evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
           source.dispatchEvent(evt);
           evt = document.createEvent("DragEvent");
           evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
           target.dispatchEvent(evt);
           evt = document.createEvent("DragEvent");
           evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
           target.dispatchEvent(evt);
           evt = document.createEvent("DragEvent");
           evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
           target.dispatchEvent(evt);
           evt = document.createEvent("DragEvent");
           evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
           source.dispatchEvent(evt);
        """, element_from, element_to)

    # общие методы
    @allure.step('клик на кнопку Создать аккаунт')
    def click_create_account(self):
        create_account = self.find_element_with_wait(MainPageLocators.click_account_button)
        self.wait_element_to_clickable(create_account)
        self.click_web_element(create_account)

    @allure.step('регистрация: ввод имени')
    def put_param_create_account(self, first_name=None, last_name=None, user_name=None, email=None, password=None):
        input_fields = self.find_elements_with_wait(MainPageLocators.input_fields)

        if not first_name: first_name = fake.first_name()
        if not last_name: last_name = fake.last_name()
        if not user_name: user_name = fake.user_name()
        if not email: email = fake.email()
        if not password: password = fake.password()

        self.add_text_to_web_element(input_fields[0], first_name)
        self.add_text_to_web_element(input_fields[1], last_name)
        self.add_text_to_web_element(input_fields[2], user_name)
        self.add_text_to_web_element(input_fields[3], email)
        self.add_text_to_web_element(input_fields[4], password)
        return [first_name, last_name, user_name, email, password]

    @allure.step('клик на кнопку создания аккаунта')
    def click_create_account_button(self):
        create_account_button = self.find_element_with_wait(MainPageLocators.click_create_account_button)
        self.wait_element_to_clickable(create_account_button)
        self.click_web_element(create_account_button)

    @allure.step('созданиe аккаунта')
    def create_account(self):
        self.click_create_account()
        account_params = self.put_param_create_account()
        self.click_create_account_button()
        return account_params

    @allure.step('ввод email')
    def put_login_email(self, email):
        self.wait_to_element(MainPageLocators.login_email)
        self.add_text_to_element(MainPageLocators.login_email, email)

    @allure.step('ввод password')
    def put_login_password(self, password):
        self.wait_to_element(MainPageLocators.login_password)
        self.add_text_to_element(MainPageLocators.login_password, password)

    @allure.step('клик на кнопку войти')
    def click_login_button(self):
        self.wait_element_to_clickable(MainPageLocators.click_login_button)
        self.click_element_locator(MainPageLocators.click_login_button)

    def login_account(self, email, password):
        self.wait_to_element(MainPageLocators.main_page_text)

        self.wait_to_element(MainPageLocators.login_email)
        self.put_login_email(email)

        self.wait_to_element(MainPageLocators.login_password)
        self.put_login_password(password)

        self.wait_element_to_clickable(MainPageLocators.click_login_button)
        self.click_login_button()