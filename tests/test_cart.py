import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

BACKPACK = "sauce-labs-backpack"
BACKPACK_NAME = "Sauce Labs Backpack"


@pytest.mark.smoke
def test_add_item_to_cart(logged_in_driver):
    inventory = InventoryPage(logged_in_driver)
    inventory.add_to_cart(BACKPACK)
    assert inventory.cart_count() == 1

    inventory.open_cart()
    cart = CartPage(logged_in_driver)
    assert cart.title() == "Your Cart"
    assert BACKPACK_NAME in cart.item_names()


@pytest.mark.regression
def test_remove_item_from_cart(logged_in_driver):
    inventory = InventoryPage(logged_in_driver)
    inventory.add_to_cart(BACKPACK)
    inventory.open_cart()

    cart = CartPage(logged_in_driver)
    cart.remove_item(BACKPACK)
    assert cart.item_names() == []


@pytest.mark.regression
def test_add_multiple_items(logged_in_driver):
    inventory = InventoryPage(logged_in_driver)
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.add_to_cart("sauce-labs-bike-light")
    assert inventory.cart_count() == 2