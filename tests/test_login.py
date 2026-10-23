import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_valid_login(driver):
    LoginPage(driver).open().login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver)
    assert "inventory" in driver.current_url
    assert inventory.title() == "Products"


@pytest.mark.regression
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("locked_out_user", "secret_sauce", "locked out"),
        ("standard_user", "wrong_password", "do not match"),
        ("", "secret_sauce", "username is required"),
        ("standard_user", "", "password is required"),
    ],
)
def test_invalid_login(driver, username, password, expected_error):
    page = LoginPage(driver).open()
    page.login(username, password)
    assert expected_error in page.error_message().lower()