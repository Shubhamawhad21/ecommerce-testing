


# 🛒 Automated Web Testing for E-commerce Website

This project is a professional end-to-end automation suite built for an e-commerce website using Selenium WebDriver, PyTest, and Allure Reports. It covers critical test scenarios such as login, product search, add-to-cart, and checkout, ensuring smooth user interactions across the site.


##  Tech Stack

- **Language**: Python 3.11+
- **Framework**: PyTest
- **Automation Tool**: Selenium WebDriver
- **Browser**: ChromeDriver
- **Reporting**: Allure Reports
- **CI/CD**: Jenkins (Optional setup)



##  Project Structure


ecommerce-testing/
├── test\_login.py          # Login test
├── test\_search.py         # Product search test
├── test\_add\_to\_cart.py    # Add to cart test
├── test\_checkout.py       # Checkout test
├── requirements.txt       # Python dependencies
├── allure-results/        # Allure raw JSON result files
├── reports/               # Generated Allure HTML reports



##  How to Run Tests

### ✅ 1. Install Dependencies

bash
pip install -r requirements.txt


### ✅ 2. Run All Tests

bash
pytest --alluredir=allure-results


### ✅ 3. Generate Allure Report (Optional)

If Allure CLI is installed:

bash
allure serve allure-results


If not installed, install using:

bash
choco install allure    # (for Windows with Chocolatey)


##  Test Cases Covered

| Test File             | Description                        |
| --------------------- | ---------------------------------- |
| `test_login.py`       | Validates user login functionality |
| `test_search.py`      | Verifies product search flow       |
| `test_add_to_cart.py` | Checks add-to-cart feature         |
| `test_checkout.py`    | Tests checkout flow and page flow  |



##  Reporting

Allure generates dynamic and detailed reports based on test execution.

* JSON results → stored in `allure-results/`
* HTML reports → stored in `reports/`

## Author

Shubham Awhad


