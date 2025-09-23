# service_layer/mycase_play_service.py
from data_layer.playwright_driver import create_playwright_context
from config.settings import DASHBOARD_URL
from parsing_layer.mycase_documents import download_case_pdfs

from config.settings import MYCASE_EMAIL, MYCASE_PASSWORD, LOGIN_URL, DASHBOARD_URL
from playwright.sync_api import TimeoutError as PlaywrightTimeout

def download_pdfs_for_case(case_id: int, subfolder: str):
    p, context, page = create_playwright_context()
    # Ir a la página de login
    page.goto(DASHBOARD_URL)
    try:
        # Espera y llena los campos
        page.fill("#login_session_email", MYCASE_EMAIL or "")
        page.fill("#login_session_password", MYCASE_PASSWORD or "")

        # Click en el botón de login
        page.click("#login-form-submit")

        # Esperar que la URL cambie a dashboard
        page.wait_for_url("**/dashboard*", timeout=15000)
        print("✅ Login exitoso en MyCase.")
        # Llamar a la función de descarga
        download_case_pdfs(page, case_id, subfolder)
    except PlaywrightTimeout:
        # Si ya estábamos logueados (por cookies), ir directo al dashboard
        page.goto(DASHBOARD_URL)
        print("ℹ️ Sesión ya activa, saltando login.")


def login_mycase():
    p, context, page = create_playwright_context()

    # Ir a la página de login
    page.goto(DASHBOARD_URL)

    try:
        # Espera y llena los campos
        page.fill("#login_session_email", MYCASE_EMAIL or "")
        page.fill("#login_session_password", MYCASE_PASSWORD or "")

        # Click en el botón de login
        page.click("#login-form-submit")

        # Esperar que la URL cambie a dashboard
        page.wait_for_url("**/dashboard*", timeout=15000)
        print("✅ Login exitoso en MyCase.")
    except PlaywrightTimeout:
        # Si ya estábamos logueados (por cookies), ir directo al dashboard
        page.goto(DASHBOARD_URL)
        print("ℹ️ Sesión ya activa, saltando login.")

    return p, context, page

def open_mycase_with_pw():
    p, context, page = create_playwright_context()
    page.goto(DASHBOARD_URL)
    print("✅ MyCase con sesión persistente (Playwright).")
    return p, context, page
