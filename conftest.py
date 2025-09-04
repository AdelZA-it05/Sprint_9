import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import data
from pages.main_page import MainPage
from pages.base_page import BasePage


@pytest.fixture
def driver():
    # Настраиваем Chrome и капабилити для удалённого запуска в Selenoid
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "128.0")
    options.set_capability(
        "selenoid:options",
        {
            # Включаем VNC и запись видео на стороне Selenoid
            "enableVNC": True,
            "enableVideo": True,
            # Имя сессии в UI и логах
            "name": os.getenv("TEST_NAME", "test_google"),
            # Детеминированное имя видеофайла
            "labels": {"videoName": os.getenv("TEST_NAME", "test_foodgram") + ".mp4"},
        },
    )

    driver = webdriver.Remote(
        # URL хаба Selenoid (из переменной окружения или значение по умолчанию)
        command_executor=os.getenv("SELENOID_URL", "http://localhost:4444/wd/hub"),
        options=options,
    )

    yield driver
    driver.quit()

@pytest.fixture
def createaccount(driver):
    driver.get(data.BASE_URL)
    createaccount = MainPage(driver).create_account()
    return createaccount

@pytest.fixture
def loginaccount(driver, createaccount):
    loginaccount = MainPage(driver).login_account(createaccount[3], createaccount[4])
    return loginaccount