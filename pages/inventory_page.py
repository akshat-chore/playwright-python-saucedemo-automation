from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_items = page.locator(".inventory_item")
        self.add_to_cart_backpack = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")

    def add_backpack_to_cart(self):
        self.add_to_cart_backpack.click()