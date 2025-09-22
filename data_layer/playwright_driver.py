from playwright.sync_api import sync_playwright

USER_DATA_DIR = r"C:\ChromeProfiles\mycase_pw"

def create_playwright_context():
    p = sync_playwright().start()
    context = p.chromium.launch_persistent_context(
        USER_DATA_DIR,
        headless=False,
        channel="chrome"  # o quita si usas Chromium
    )
    page = context.new_page()
    return p, context, page
