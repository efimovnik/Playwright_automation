import os
import time
import pytest
from playwright.sync_api import expect

PASSWORD = os.environ['PASSWORD']


def set_up(page):
    # Arrange - Giver
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    yield page


@pytest.fixture(scope="session")
def context_creation(playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=300)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    login_issue = True
    while login_issue:
        if not page.get_by_test_id("signUp.switchToSignUp").is_visible():
            page.get_by_text("Log In").click()
        else:
            login_issue = False
        time.sleep(0.1)
    # page.get_by_text("Log In").click()
    # page.wait_for_selector("signUp.switchToSignUp")
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_test_id("siteMembersDialogLayout").get_by_test_id("buttonElement").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill("train.supersonic@gmail.com")
    # page.get_by_label("Password").fill(utils.secret_config.PASSWORD)
    page.get_by_label("Password").fill(PASSWORD)
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    # page.wait_for_load_state('networkidle')
    time.sleep(2)
    context.storage_state(path='state.json')
    yield context


@pytest.fixture()
def login_set_up(context_creation, browser):
    context = browser.new_context(storage_state='state.json')
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    expect(page.get_by_text("Log In")).not_to_be_visible()
    yield page
    page.close()