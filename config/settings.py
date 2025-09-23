# config/settings.py
# Configuración para el scraping con Selenium y Chrome
import os
from dotenv import load_dotenv

EMAIL_TO_CHROME_PROFILE = {
    "jo.miranda@mendozafirm.com": "Profile 1",
    # Agrega más correos y perfiles si es necesario
}

load_dotenv()  # lee el archivo .env
MYCASE_EMAIL = os.getenv("MYCASE_EMAIL")
MYCASE_PASSWORD = os.getenv("MYCASE_PASSWORD")
DASHBOARD_URL = "https://the-mendoza-law-firm.mycase.com/dashboard"
LOGIN_URL = "https://auth.mycase.com/login_sessions/new?response_type=code&client_id=tCEM8hNY7GaC2c8P&redirect_uri=https%3A%2F%2Fthe-mendoza-law-firm.mycase.com%2Fuser_sessions%2Fo_auth_callback&login_required=true"

BASE_CASE_URL = "https://the-mendoza-law-firm.mycase.com/court_cases"
DOWNLOAD_DIR = r"C:\MyCaseDownloads"

CHROME_USER_DATA_BASE = r"C:\Users\HoneyMaldonado\AppData\Local\Google\Chrome\User Data"

LOGIN_URL = ("https://www.mycase.com/login/")
DEBUGGER_ADDRESS = "127.0.0.1:9222"
