import time
import pytest
from playwright.sync_api import expect


@pytest.mark.integration
def test_login(login_set_up) -> None:
    page = login_set_up
    page.get_by_role("button", name="train.supersonic account menu").click()
    page.get_by_role("link", name="My Account").click()

    # Assert - Then
    expect(page.locator("//div[text()='Login Email']/following-sibling::div[1]")).to_have_text(
        "train.supersonic@gmail.com")