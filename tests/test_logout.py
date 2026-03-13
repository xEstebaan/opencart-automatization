from pages.base_page import BasePage
from components.top_nav import Top_nav
from pages.login_page import LoginPage


def test_logout(driver_session):
    login_page = LoginPage(driver_session)
    login_page.navigate()
    login_page.login("testAdmin1!", "testAdmin1!")
    top_nav = Top_nav(driver_session)
    top_nav.select_logout_option()

    assert (
        "/auth/login" in BasePage(driver_session).get_current_url()
    ), "do not redirect"


def test_try_access_by_back(driver_session):
    base_page = BasePage(driver_session)
    base_page.back()
    current_url = base_page.get_current_url()

    assert (
        "/auth/login" in current_url
    ), f"Error: driver not redirect to /login current url: {current_url}"


def test_try_access_by_url(driver_session):
    base_page = BasePage(driver_session)
    base_page.open("/web/index.php/time/viewTimeModule")

    assert (
        "/auth/login" in BasePage(driver_session).get_current_url()
    ), "do not redirect"
