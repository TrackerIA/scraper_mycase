# service_layer/mycase_service.py
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data_layer.selenium_driver import attach_to_running_chrome
from config.settings import DASHBOARD_URL

def use_existing_session():
    driver = attach_to_running_chrome()
    wait = WebDriverWait(driver, 20)

    time.sleep(0.8)
    driver.get("about:blank")
    time.sleep(0.4)
    driver.get(DASHBOARD_URL)

    # Verificación mínima por URL
    wait.until(EC.url_contains("mycase.com"))
    print("✅ Sesión válida y dashboard cargado.")
    return driver
