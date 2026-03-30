import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

# ── Setup & Teardown ──────────────────────────────────────────────
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

# ── Test Cases ────────────────────────────────────────────────────

def test_valid_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url, "Valid login failed"

def test_invalid_password(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "wrong_password")
    error = page.get_error_message()
    assert "Username and password do not match" in error

def test_locked_out_user(driver):
    page = LoginPage(driver)
    page.open()
    page.login("locked_out_user", "secret_sauce")
    error = page.get_error_message()
    assert "locked out" in error

def test_empty_fields(driver):
    page = LoginPage(driver)
    page.open()
    page.click_login()
    error = page.get_error_message()
    assert "Username is required" in error

def test_empty_password(driver):
    page = LoginPage(driver)
    page.open()
    page.enter_username("standard_user")
    page.click_login()
    error = page.get_error_message()
    assert "Password is required" in error