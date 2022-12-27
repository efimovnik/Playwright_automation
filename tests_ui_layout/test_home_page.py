from pom.home_page_elements import HomePage
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


@pytest.mark.smoke
def test_home_page(login_set_up):
    # Assess - Given
    page = login_set_up
    # Assert
    expect(HomePage(page).celebrating_header).to_be_visible()
    expect(HomePage(page).celebrating_body).to_be_visible()


@pytest.mark.regression
@pytest.mark.xfail(reason="demonstrate fail")
def test_home_page_2(login_set_up):
    # Assess - Given
    page = login_set_up
    # Assert
    expect(HomePage(page).celebrating_header).to_be_visible()
    expect(HomePage(page).celebrating_body).to_be_visible()