import os
import time
import pytest

try:
    PASSWORD = os.environ['PASSWORD']
except KeyError:
    import utils.secret_config
    PASSWORD = utils.secret_config.PASSWORD


@pytest.fixture(scope="session")
def set_up(browser):
    # Arrange - Giver
    # browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    yield page


@pytest.fixture(scope="session")
def login_set_up(set_up):
    page = set_up
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
    yield page
    page.close()
