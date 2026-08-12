# Playwright Python – SauceDemo Automation Framework

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-Automation-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testing-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

Automated UI test suite for [SauceDemo](https://www.saucedemo.com/) built with **Playwright + Python + Pytest**, using the **Page Object Model (POM)** design pattern.

This project was built to practice and demonstrate Python-based test automation skills, following a project previously implemented in Playwright + TypeScript.

---

## 🛠 Tech Stack

- **Language:** Python 3.11
- **Automation:** Playwright (sync API)
- **Test Runner:** Pytest
- **Fixtures/Integration:** pytest-playwright
- **Reporting:** pytest-html

---

## 📁 Project Structure

```
playwright-python-saucedemo/
├── pages/                  # Page Object classes
│   ├── login_page.py
│   ├── inventory_page.py
│   └── checkout_page.py
├── tests/                  # Test cases
│   ├── test_login.py
│   ├── test_inventory.py
│   └── test_checkout.py
├── conftest.py             # Shared fixtures (e.g. logged_in_page)
├── pytest.ini              # Pytest configuration
├── requirements.txt        # Project dependencies
└── README.md
```

---

## ✅ Features Covered

- Login with valid credentials
- Negative test — locked-out user error handling
- Add item to cart
- End-to-end checkout flow (info form → order confirmation)

---

## ⚙️ Setup & Installation

```bash
git clone https://github.com/<your-username>/playwright-python-saucedemo-automation.git
cd playwright-python-saucedemo-automation

python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

pip install -r requirements.txt
playwright install
```

---

## ▶️ Running Tests

```bash
# Run all tests
pytest -v

# Run in headed mode (see the browser interact live)
pytest -v --headed

# HTML report is generated automatically after each run → report.html
```

---

## 🧩 Design Notes

- Built using the **Page Object Model (POM)** pattern to keep locators/actions separate from test logic, improving maintainability and readability.
- Locators use `data-test` attributes — the most stable selector strategy for this app, confirmed by cross-checking manually written locators against **Playwright Codegen** output.
- `conftest.py` provides a reusable `logged_in_page` fixture so login steps aren't repeated across every test file.
- Each test runs in an isolated browser context (via `pytest-playwright`'s `page` fixture), so tests have no shared state and can run in any order.

---

## 📌 Roadmap

- [ ] Add `pytest.mark` markers (smoke / regression) for suite subsets
- [ ] Integrate GitHub Actions for CI
- [ ] Expand coverage — sorting, cart removal, multiple checkout scenarios

---

## 👤 Author

**Akshat**
QA / SDET Engineer 