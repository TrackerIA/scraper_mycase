# data_layer/selenium_driver.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.settings import EMAIL_TO_CHROME_PROFILE, CHROME_USER_DATA_BASE, MYCASE_EMAIL, DASHBOARD_URL
from data_layer.driver_validator import validate_versions
from time import sleep
from selenium.common.exceptions import WebDriverException
from config.settings import DEBUGGER_ADDRESS

def attach_to_running_chrome():
    options = webdriver.ChromeOptions()
    # Solo la opción de debug para adjuntar
    options.add_experimental_option("debuggerAddress", DEBUGGER_ADDRESS)
    options.add_argument("--remote-allow-origins=*")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def create_driver():
    if not validate_versions():
        print("⚠️ Versiones de Chrome/Driver no coinciden. Intentando continuar...")

    options = webdriver.ChromeOptions()
    options.add_argument("--remote-allow-origins=*")  # 🔑 Importante
    profile_name = EMAIL_TO_CHROME_PROFILE.get(MYCASE_EMAIL, "Default")
    options.add_argument(f"--user-data-dir={CHROME_USER_DATA_BASE}")
    options.add_argument(f"--profile-directory={profile_name}")

    # O usa la versión exacta si falla la genérica
    service = Service(ChromeDriverManager("140.0.7339.186").install())
    driver = webdriver.Chrome(service=service, options=options)
    options.add_argument("--new-window")
    driver = webdriver.Chrome(service=service, options=options)
    driver.switch_to.new_window('tab')
    sleep(3)
    driver.get(DASHBOARD_URL)

    return driver
