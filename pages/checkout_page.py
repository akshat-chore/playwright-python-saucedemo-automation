from playwright.sync_api import Page 

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator("[data-test='checkout']")
        self.firstName_input = page.locator("[data-test='firstName']")
        self.lastName_input = page.locator("[data-test='lastName']")
        self.postalCode_input = page.locator("[data-test='postalCode']")
        self.continueButton = page.locator("[data-test='continue']")
        self.finishButton = page.locator("[data-test='finish']")
        self.completeHeader= page.locator("[data-test='complete-header']")

    def start_checkout(self):
        self.checkout_button.click()
    
    def fill_info(self, firstName: str, lastName: str, postalCode: str):
        self.firstName_input.fill(firstName)
        self.lastName_input.fill(lastName)
        self.postalCode_input.fill(postalCode)
        self.continueButton.click()

    def finish(self):
        self.finishButton.click()


