from pages.login_page import LoginPage
from pages.base_page import BasePage


def test_login_admin_success(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.login("testAdmin1!", "testAdmin1!")

    assert (
        "/dashboard/index" in BasePage(driver).get_current_url()
    ), "Login failed, not redirected to Dashboard"


def test_login_empty_credentials(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.login("", "")

    request_error = login_page.wait_for_elements(LoginPage.REQUIRED_FIELD_ERROR)

    assert (
        "/auth/login" in BasePage(driver).get_current_url()
    ), "Login should fail with empty credentials, but it succeeded"

    assert len(request_error) == 2, "Expected errors messages not found"


def test_login_invalid_username(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.login("invalidUser", "testAdmin1!")

    assert (
        "/auth/login" in BasePage(driver).get_current_url()
    ), "Login should fail with invalid username, but it succeeded"

    assert login_page.is_visible(
        LoginPage.INVALID_CREDENTIALS_ERROR
    ), "Expected error message not found"

    assert "Invalid credentials" in login_page.get_text(
        LoginPage.INVALID_CREDENTIALS_ERROR
    ), "Expected error message not found"


def test_login_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.login("testAdmin1!", "invalidPass")
    assert (
        "/auth/login" in BasePage(driver).get_current_url()
    ), "Login should fail with invalid password, but it succeeded"
    assert login_page.is_visible(
        LoginPage.INVALID_CREDENTIALS_ERROR
    ), "Expected error message not found"
    assert "Invalid credentials" in login_page.get_text(
        LoginPage.INVALID_CREDENTIALS_ERROR
    ), "Expected error message not found"
