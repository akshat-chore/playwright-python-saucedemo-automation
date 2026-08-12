from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage


def test_add_item_to_cart(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_backpack_to_cart()

    expect(inventory_page.cart_badge).to_have_text("1")