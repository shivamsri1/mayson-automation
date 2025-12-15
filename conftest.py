import os
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    is_ci = os.getenv("CI", "false").lower() == "true"

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=is_ci,   # 👈 CI = headless, Local = headed
            slow_mo=500 if not is_ci else 0
        )
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()
