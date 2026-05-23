"""GitHub repository page object."""

import re

from playwright.sync_api import expect

from pages.base_page import BasePage


class RepositoryPage(BasePage):
    """Page Object for a GitHub repository page."""

    README_WITH_TEXT_XPATH_TEMPLATE = (
        "//*[@id='readme']//article["
        "contains(@class, 'markdown-body') "
        "and contains(., '{text}')"
        "]"
        " | //article["
        "contains(@class, 'markdown-body') "
        "and contains(., '{text}')"
        "]"
    )

    def should_be_opened(self, owner: str, repo: str) -> None:
        """Assert that the expected repository page is opened."""
        url_pattern = re.compile(
            rf"https://github\.com/{owner}/{repo}(/.*)?$"
        )
        expect(self.page).to_have_url(url_pattern)

    def should_contain_readme_text(self, text: str) -> None:
        """Assert that README.md contains the expected text."""
        readme_locator = self.xpath(
            self.README_WITH_TEXT_XPATH_TEMPLATE.format(text=text)
        ).first
        readme_locator.wait_for(state="attached")
        expect(readme_locator).to_contain_text(text)
