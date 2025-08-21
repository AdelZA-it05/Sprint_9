from selenium.webdriver.common.by import By

class RecipePageLocators:

    click_create_recipe = By.XPATH, "//a[text()='Создать рецепт']"  # tab создать рецепт

    recipe_fields = By.XPATH, "//input[@class[contains(.,'styles_inputField__3eqTj')]]"  # список полей создания рецепта
    recipe_text = By.XPATH, "//textarea[@class= 'styles_textareaField__1wfhC']"  # описание рецепта
    ingredients_list = By.XPATH, "//div[@class= 'styles_container__3ukwm']"  # список ингредиентов при вводе/поиске
    click_add_ingredient = By.XPATH, "//div[@class='styles_ingredientAdd__3fc32']"  # кнопка добавить ингредиент
    ingredient_div = By.XPATH, "//div"  #

    form_input_file = By.XPATH, "//div[@class='styles_button__xzu5F']"  # форма выбор файла с фото рецепта
    input_file = By.XPATH, "//input[@class='styles_fileInput__3HjP3']"  # выбор файла с фото рецепта

    button_create_recipe = By.XPATH, "//button[text()='Создать рецепт']"  # кнопка войти на главной странице

    recipe_card_name = By.XPATH, "//h1[@class='styles_single-card__title__2QMPq']"  # карточка рецепта: наименование
    recipe_card_edit = By.XPATH, "//a[@class[contains(.,'style_link__1kPh8 styles_single-card__edit__Mb_wc')]]"  # карточка рецепта: редактирование