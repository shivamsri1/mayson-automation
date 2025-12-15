from pages.login_page import LoginPage
from utils.test_data import VALID_EMAIL, VALID_PASSWORD

def test_login_valid_user(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(VALID_EMAIL, VALID_PASSWORD)

    # Simple validation: URL should change after login
    page.wait_for_timeout(3000)
    assert "login" not in page.url
