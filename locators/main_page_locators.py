from selenium.webdriver.common.by import By

class MainPageLocators:
    main_page_text = By.XPATH, "//h1[text()='Войти на сайт']"  # текст войти на сайт на главной странице
    click_login_button = By.XPATH, "//button[text()='Войти']"  # кнопка войти на главной странице
    click_logout_button = By.XPATH, "//a[text()='Выход']"  # кнопка выход
    main_page_recipes_text = By.XPATH, "//h1[text()='Рецепты']"  # текст рецепты на главной странице

    click_account_button = By.XPATH, "//a[text()='Создать аккаунт']" # создать аккаунт
    click_create_account_button = By.XPATH, "//button[text()='Создать аккаунт']"  # создание аккаунта
    input_fields = By.XPATH, "//input[@class= 'styles_inputField__3eqTj']"  # список полей регистрации аккаунта
    login_email = By.XPATH, "//input[@name='email']"  # авторизация: ввод email
    login_password = By.XPATH, "//input[@name='password']"  # авторизация: ввод password
