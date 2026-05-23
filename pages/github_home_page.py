"""GitHub home page object."""

from urllib.parse import quote_plus

from pages.base_page import BasePage
from pages.search_results_page import SearchResultsPage


class GitHubHomePage(BasePage):
    """Page object for GitHub main page."""

    SEARCH_INPUT_XPATH = (
        "//input[@type='text' and "
        "("
        "contains(@id, 'query-builder') "
        "or contains(@name, 'query-builder') "
        "or @name='q' "
        "or contains(@aria-label, 'Search') "
        "or contains(@placeholder, 'Search')"
        ")]"
    )

    def open_home_page(self) -> None:
        """Open GitHub home page."""
        self.open("/")
        self.page.wait_for_load_state("domcontentloaded")

    def search_for(self, text: str) -> SearchResultsPage:
        """
        Search repository by text from GitHub global search.

        First, the method tries to use GitHub UI search.
        If GitHub keeps the input hidden, the method opens
        the same search results page directly.
        """
        try:
            self.page.locator("body").click()
            self.page.keyboard.press("/")

            search_input = self.first_visible_xpath(
                self.SEARCH_INPUT_XPATH,
                timeout=3000,
            )
            search_input.fill(text)
            search_input.press("Enter")

            self.page.wait_for_url("**/search**", timeout=15000)

        except AssertionError:
            query = quote_plus(text)
            self.page.goto(
                f"{self.BASE_URL}/search?q={query}&type=repositories",
                wait_until="domcontentloaded",
            )

        return SearchResultsPage(self.page)