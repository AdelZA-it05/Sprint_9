import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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
    # Дадим Selenoid время завершить запись видео
    time.sleep(1)
    driver.quit()