from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    @staticmethod
    def _add_button(product_slug):
        return (By.ID, f"add-to-cart-{product_slug}")

    def title(self):
        return self.text_of(self.TITLE)

    def product_names(self):
        return self.texts_of(self.ITEM_NAMES)

    def add_to_cart(self, product_slug):
        """product_slug example: 'sauce-labs-backpack'"""
        self.click(self._add_button(product_slug))

    def cart_count(self):
        if self.is_visible(self.CART_BADGE):
            return int(self.text_of(self.CART_BADGE))
        return 0

    def open_cart(self):
        self.click(self.CART_LINK)