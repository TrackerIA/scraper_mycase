#python scripts/seed_playwright_profile.py
from playwright.sync_api import sync_playwright

USER_DATA_DIR = r"C:\ChromeProfiles\mycase_pw"

with sync_playwright() as p:
    # Creamos el contexto persistente (perfil permanente)
    context = p.chromium.launch_persistent_context(
        USER_DATA_DIR,
        headless=False,          # Necesitamos ver la ventana
        channel="chrome"         # Opcional: usa Chrome en vez de Chromium
    )
    page = context.new_page()
    page.goto("https://the-mendoza-law-firm.mycase.com/dashboard")

    print("➡️  Se abrió el navegador.")
    print("👉  Inicia sesión en MyCase, completa el 2FA y marca 'Recordar este dispositivo'.")
    input("Cuando veas el dashboard y hayas terminado, pulsa ENTER aquí para cerrar.")

    context.close()
