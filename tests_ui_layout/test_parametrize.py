import time
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


@pytest.mark.parametrize("email", ["train.supersonic@gmail.com",
                                   pytest.param("train.supersonic", marks=pytest.mark.xfail),])
@pytest.mark.parametrize("password", ["Playwrighttest123",
                                      pytest.param("", marks=pytest.mark.xfail)])
@pytest.mark.integration
def test_login_parametrize(page, email, password) -> None:
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    login_issue = True
    while login_issue:
        if not page.get_by_test_id("signUp.switchToSignUp").is_visible():
            page.get_by_text("Log In").click()
        else:
            login_issue = False
        time.sleep(0.1)
    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_test_id("siteMembersDialogLayout").get_by_test_id("buttonElement").click()
    page.get_by_test_id("emailAuth").get_by_label("Email").fill(email)
    page.get_by_label("Password").fill(password)
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    page.wait_for_selector("//button[@aria-label='train.supersonic account menu']", timeout=3000)
    page.get_by_role("button", name="train.supersonic account menu").click()
    page.get_by_role("link", name="My Account").click()

    # Assert - Then
    expect(page.locator("//div[text()='Login Email']/following-sibling::div[1]")).to_have_text(
        email)
