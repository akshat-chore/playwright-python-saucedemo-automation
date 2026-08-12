from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

def test_complete_checkout_process(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_backpack_to_cart()
    inventory_page.cart_link.click()

    checkout_page = CheckoutPage(logged_in_page)
    checkout_page.start_checkout()
    checkout_page.fill_info("John", "Doe", "12345")
    checkout_page.finish()

    expect(checkout_page.completeHeader).to_have_text("Thank you for your order!")
    





