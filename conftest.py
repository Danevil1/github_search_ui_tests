"""PyTest fixtures for UI tests."""

import os

import pytest
from playwright.sync_api import Browser, Page, sync_playwright


@pytest.fixture(scope="session")
def browser() -> Browser:
    """Start Chrome browser for the whole test session."""
    headless = os.getenv("HEADLESS", "true").lower() != "false"

    with sync_playwright() as playwright:
        browser_instance = playwright.chromium.launch(
            channel="chrome",
            headless=headless,
        )
        yield browser_instance
        browser_instance.close()


@pytest.fixture()
def page(browser: Browser) -> Page:
    """Create a clean browser context and page for each test."""
    context = browser.new_context(
        locale="en-US",
        viewport={"width": 1440, "height": 1000},
    )
    test_page = context.new_page()
    test_page.set_default_timeout(15_000)

    yield test_page

    context.close()
