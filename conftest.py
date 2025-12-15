import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,   # 👈 SHOW browser
            slow_mo=500       # 👈 slow actions (optional)
        )
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()
