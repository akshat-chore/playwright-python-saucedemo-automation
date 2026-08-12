# Playwright Python – SauceDemo Automation Framework

Automated UI test suite for [SauceDemo](https://www.saucedemo.com/) built with **Playwright + Python + Pytest**, using the **Page Object Model (POM)** design pattern.

This project was built to practice and demonstrate Python-based test automation skills, following a project I previously implemented in Playwright + TypeScript.

## Tech Stack
- Python 3.11
- Playwright (sync API)
- Pytest
- pytest-playwright
- pytest-html (reporting)

## Project Structure
playwright-python-saucedemo/
├── pages/ # Page Object classes
│ ├── login_page.py
│ ├── inventory_page.py
│ └── checkout_page.py
├── tests/ # Test cases
│ ├── test_login.py
│ ├── test_inventory.py
│ └── test_checkout.py
├── conftest.py # Shared fixtures (e.g. logged_in_page)
├── pytest.ini # Pytest config
└── requirements.txt

## Features Covered
- Login (valid credentials + locked-out user negative test)
- Add item to cart
- End-to-end checkout flow

## Setup & Installation

```bash
git clone https://github.com/<your-username>/playwright-python-saucedemo-automation.git
cd playwright-python-saucedemo-automation

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
playwright install
```

## Running Tests

```bash
# Run all tests
pytest -v

# Run in headed mode (see the browser)
pytest -v --headed

# Generates report.html automatically after run
```

## Design Notes
- Uses the **Page Object Model** to separate locators/actions from test logic.
- Uses `data-test` attributes for locators — the most stable selector strategy for this app, confirmed by comparing manually-written locators against Playwright Codegen output.
- `conftest.py` provides a `logged_in_page` fixture to avoid repeating login steps across test files.