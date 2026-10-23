from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BTN = (By.ID, "checkout")

    @staticmethod
    def _remove_button(product_slug):
        return (By.ID, f"remove-{product_slug}")

    def title(self):
        return self.text_of(self.TITLE)

    def item_names(self):
        if not self.driver.find_elements(*self.CART_ITEMS):
            return []
        return self.texts_of(self.ITEM_NAMES)

    def remove_item(self, product_slug):
        self.click(self._remove_button(product_slug))

    def checkout(self):
        self.click(self.CHECKOUT_BTN)