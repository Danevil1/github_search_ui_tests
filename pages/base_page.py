"""Base Page Object with shared helpers."""

from urllib.parse import urljoin

from playwright.sync_api import Locator, Page, expect


class BasePage:
    """Base class for all page objects."""

    BASE_URL = "https://github.com"

    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self, path: str = "/") -> None:
        """Open a GitHub page by relative path."""
        url = urljoin(self.BASE_URL, path)
        self.page.goto(url, wait_until="domcontentloaded")

    def xpath(self, expression: str) -> Locator:
        """Return a locator by XPath expression."""
        return self.page.locator(f"xpath={expression}")

    def first_visible_xpath(self, expression: str) -> Locator:
        """Return the first visible element found by XPath."""
        locator = self.xpath(expression).first
        locator.wait_for(state="visible")
        return locator

    def should_have_url_matching(self, pattern: object) -> None:
        """Assert the current page URL matches a string or regex pattern."""
        expect(self.page).to_have_url(pattern)
