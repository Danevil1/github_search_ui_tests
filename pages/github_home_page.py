"""GitHub home page object."""

import re

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from pages.base_page import BasePage
from pages.search_results_page import SearchResultsPage


class GitHubHomePage(BasePage):
    """Page Object for https://github.com."""

    SEARCH_FIELD_OR_TRIGGER_XPATH = (
        "//button["
        "contains(@class, 'header-search-button') "
        "or contains(@aria-label, 'Search') "
        "or contains(normalize-space(.), 'Search') "
        "or contains(normalize-space(.), 'Type / to search')"
        "]"
        " | //input["
        "@name='q' "
        "and (contains(@placeholder, 'Search') "
        "or contains(@aria-label, 'Search'))"
        "]"
    )

    SEARCH_INPUT_XPATH = (
        "//input["
        "@name='q' "
        "and (contains(@placeholder, 'Search') "
        "or contains(@aria-label, 'Search'))"
        "]"
        " | //input["
        "contains(@id, 'query-builder') "
        "or contains(@aria-label, 'Search') "
        "or contains(@placeholder, 'Search')"
        "]"
    )

    SEARCH_URL_PATTERN = re.compile(r"https://github\.com/search.*q=.*copilot.*")

    def search_for(self, keyword: str) -> SearchResultsPage:
        """Search for a keyword through the global search input."""
        search_element = self.first_visible_xpath(self.SEARCH_FIELD_OR_TRIGGER_XPATH)
        search_element.click()

        search_input = self.first_visible_xpath(self.SEARCH_INPUT_XPATH)
        search_input.fill(keyword)
        search_input.press("Enter")

        try:
            self.page.wait_for_url(self.SEARCH_URL_PATTERN, timeout=10_000)
        except PlaywrightTimeoutError:
            # GitHub may keep focus in the query builder after the first Enter.
            # A second Enter confirms the typed query in some UI versions.
            search_input.press("Enter")
            self.page.wait_for_url(self.SEARCH_URL_PATTERN, timeout=10_000)

        self.page.wait_for_load_state("domcontentloaded")
        return SearchResultsPage(self.page)
